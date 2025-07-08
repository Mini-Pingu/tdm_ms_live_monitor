import os
import whisper
import librosa
import numpy as np

import noisereduce as nr  # 若需降噪

from openai import OpenAI
from pydub import AudioSegment


from app.core.config import config
from app.core.logger import logger


class PostHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def audio_handler():
        aac_files = sorted(
            [f for f in os.listdir(config.temp_folder) if f.endswith(".aac")],
            key=lambda x: int(x.split(".")[0].split("_")[-1]),
        )
        logger.info(f"Found {len(aac_files)} audio files")

        processed_chunks = []
        for file in aac_files:
            audio_path = os.path.join(config.temp_folder, file)
            try:
                if file.endswith(".aac"):
                    audio = AudioSegment.from_file(audio_path, format="aac")
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
            **{
                "word_timestamps": config.whisper_word_timestamps,
                "temperature": config.whisper_temperature,
                "temperature_increment_on_fallback": config.whisper_temperature_increment_on_fallback,
            },
        )
        audio_path = os.path.join(config.temp_folder, config.temp_mp3)

        if not os.path.exists(audio_path):
            logger.error(f"Audio file {audio_path} does not exist.")
            return None

        result = model.transcribe(
            audio=audio_path,
            language="zh",
            task="transcribe",
            fp16=True,
            initial_prompt=config.initial_prompt,
        )

        return result

    @staticmethod
    def llm_handler(text: str):
        logger.info(f"Starting LLM processing")
        client = OpenAI(
            api_key=config.llm_api_key, base_url="https://api.perplexity.ai"
        )
        response = client.chat.completions.create(
            model=config.llm_model,  # 可选模型，按需更换
            messages=[
                {
                    "role": "user",
                    "content": f"{text} ||| 以上是電臺節目語音識別內容，我只要分析這段內容，給我標題，內容（內容字數一定要 700字 以上，並且要對內容要各點進行最詳細的總結，不包括主题点分析的字数，內容要列點說明， 1 2 34 這樣子，並且因爲我要輸入的地方只接受純文本，所以 1 2 3 4 5 這些列點要整理好），和主題點分析（要有起碼5點以上，要有标题和30字以上的解释）。總結和主題點分析出來的內容不要太多專業術語，因爲看的內容是普通市民（这个一定要注意），但是一定要貼近原有文本，并且要说明是从这个节目中分析出来为主，而不是直接分析内容。並且結合聯網功能搜索出來的內容比例要減少到最多 40% 就夠。全部內容文字中不要出現搜索來源等的提示，因爲我要直接複製粘貼的。我不要複製到什麼搜索結果等文字出來。",
                }
            ],
        )
        return response.model_dump()


post_handler = PostHandler()
