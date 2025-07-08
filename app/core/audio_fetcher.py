import requests
from app.core.config import config


class AudioFetcher(object):
    def __init__(self):
        pass

    @staticmethod
    def chunk_list_handler():
        """
        Fetch the audio data from the TDM live program URL.
        """
        try:
            response = requests.get(
                config.tdm_online_feed_url, headers=config.headers, timeout=5
            )
            response.raise_for_status()
            lines = [
                line.strip()
                for line in response.text.splitlines()
                if line.startswith("chunklist")
            ]
            return lines[0]

        except requests.RequestException as e:
            print(f"Error fetching audio data: {e}")
            return None

    @staticmethod
    def audio_list_handler(chunk_list):
        """
        Fetch the audio list from the TDM live chunk list base URL.
        """
        try:
            response = requests.get(
                f"{config.tdm_live_chunk_list_base_url}/{chunk_list}",
                headers=config.headers,
                timeout=5,
            )
            response.raise_for_status()
            lines = [
                line.strip()
                for line in response.text.splitlines()
                if line.startswith("media")
            ]
            return lines[-1]

        except requests.RequestException as e:
            print(f"Error fetching audio list: {e}")
            return None

    @staticmethod
    def audio_handler(audio_name):
        """
        Fetch the audio data from the TDM live audio base URL.
        """
        try:
            response = requests.get(
                f"{config.tdm_live_audio_base_url}/{audio_name}",
                headers=config.headers,
                timeout=5,
            )
            response.raise_for_status()
            with open(f"{config.temp_folder}/{audio_name}", "wb") as audio_file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        audio_file.write(chunk)
            return audio_name
        except requests.RequestException as e:
            print(f"Error fetching audio data: {e}")
            return None
