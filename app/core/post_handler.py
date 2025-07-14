import os
import re
import whisper
import librosa
import datetime
import numpy as np

import noisereduce as nr  # 若需降噪

from openai import OpenAI
from pydub import AudioSegment

from app.core.config import config
from app.core.logger import logger
from app.core.utils import utils
from app.core.llm import llm_handler


class PostHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def audio_handler():
        audio_files = sorted(
            [
                f
                for f in os.listdir(config.temp_folder)
                if f.endswith(f".{config.temp_file_extension}")
            ],
            key=lambda x: int(x.split(".")[0].split("_")[-1]),
        )
        logger.info(f"====================================")
        logger.info(f"Found {len(audio_files)} audio files")

        processed_chunks = []
        for file in audio_files:
            audio_path = os.path.join(config.temp_folder, file)
            try:
                if file.endswith(f".{config.temp_file_extension}"):
                    audio = AudioSegment.from_file(
                        audio_path, format=config.temp_file_extension
                    )
                    wav_path = os.path.join(
                        config.temp_folder, f"{os.path.splitext(file)[0]}.wav"
                    )
                    audio.export(wav_path, format="wav")
                    audio, sr = librosa.load(wav_path, sr=16000, mono=True)
                    audio_float32 = audio.astype(np.float32)
                    audio_denoised = nr.reduce_noise(y=audio_float32, sr=sr)
                    processed_chunks.append(audio_denoised)
            except Exception as e:
                logger.error(f"Failed to process {file}: {e}")

        combined_audio_np = np.concatenate(processed_chunks)
        if combined_audio_np.dtype != np.int16:
            combined_audio_np = (combined_audio_np * 32767).astype(np.int16)
        combined = AudioSegment(
            combined_audio_np.tobytes(),
            frame_rate=16000,
            sample_width=combined_audio_np.dtype.itemsize,
            channels=1,
        )

        # 轉換為 WAV
        output_wav_path = os.path.join(config.temp_folder, config.temp_wav)
        combined.export(output_wav_path, format="wav")
        logger.info(f"Converted WAV saved to: {output_wav_path}")

    @staticmethod
    def asr_handler():
        logger.info(f"Starting ASR")
        model = whisper.load_model(
            config.whisper_model_version,
            device="cuda",
        )
        audio_path = os.path.join(config.temp_folder, config.temp_wav)

        if not os.path.exists(audio_path):
            logger.error(f"Audio file {audio_path} does not exist.")
            return None

        logger.info(f"Transcribing audio file: {audio_path}")
        result = model.transcribe(
            audio=audio_path,
            language="zh",
            task="transcribe",
            fp16=True,
            initial_prompt=config.initial_prompt,
            word_timestamps=config.whisper_word_timestamps,
            temperature=config.whisper_temperature,
            beam_size=config.whisper_beam_size,
            best_of=config.whisper_best_of,
        )

        sentences = result["segments"]
        total_text = ""
        dialogs = []

        grouped = {}
        for sentence in sentences:
            start_interval = int(sentence["start"] // config.interval) * config.interval
            end_interval = start_interval + config.interval
            key = (start_interval, end_interval)

            if key not in grouped:
                grouped[key] = []
            grouped[key].append(sentence["text"].strip())

        for (start, end), texts in sorted(grouped.items()):
            time_str = utils.format_interval(start)
            combined_text = " ".join(texts)
            combined_text = combined_text.replace("\n", "")
            fine_tuned_text = llm_handler.analysis(
                text=combined_text, prompt=config.sentence_format_prompt
            )
            total_text += fine_tuned_text
            dialog = {
                "timeStr": time_str,
                "content": fine_tuned_text,
            }

            dialogs.append(dialog)

        return dialogs, total_text

    @staticmethod
    def analyze_handler(text: str = ""):
        logger.info(f"Starting LLM processing")
        analyze_response = llm_handler.analysis(
            model=config.llm_model, text=text, prompt=config.llm_prompt
        )
        result_response = llm_handler.analysis(
            model=config.llm_text_format_model,
            text=analyze_response,
            prompt=config.llm_text_format_prompt,
        )
        return utils.extract_json_from_text(result_response)

    @staticmethod
    def output_handler(dialog_text, analyzed_text):
        """
        Outputs the processed dialog text and analyzed text to a file.
        """
        output = {}
        audio_path = os.path.join(config.temp_folder, config.temp_wav)
        output["title"] = analyzed_text["title"]
        output["sumarization"] = analyzed_text["sumarization"]
        output["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output["source"] = config.source
        output["dialogs"] = dialog_text
        output["audioFrequencyData"] = utils.convert_audio_base64(audio_path)
        output["subjects"] = analyzed_text["subjects"]
        return output


post_handler = PostHandler()
