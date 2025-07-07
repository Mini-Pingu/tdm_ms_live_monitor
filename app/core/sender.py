import requests
from app.core.config import Config
from app.core.utils import utils


class Sender:
    def __init__(self):
        self.wild_box_url = Config.wild_box_url

    def send(self, meta, audio):
        """
        Sends data to the Wild Box API.

        :param meta: Dictionary containing metadata about the audio.
        :param audio: Path to the audio file to be sent.
        :return: Response from the API.
        """

        data = {
            "title": meta.get("title", ""),
            "sumarization": meta.get("sumarization", ""),
            "date": meta.get("date", ""),
            "source": meta.get("source", ""),
            "audioFrequencyData": utils.convert_audio_base64(audio),
            "dialogs": meta.get("dialogs", []),
            "subjects": meta.get("subjects", []),
        }

        try:
            response = requests.post(self.wild_box_url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending data: {e}")
            return None
