import requests

from app.core.logger import logger
from app.core.utils import utils
from app.core.config import config


class Sender:

    @staticmethod
    def send(payload: dict) -> dict:
        """
        Sends data to the Wild Box API.

        :param payload: A dictionary containing the data to be sent.
        :return: Response from the API.
        """

        logger.info("Sending data to Wild Box API...")
        data = {
            "title": payload.get("title", ""),
            "sumarization": payload.get("sumarization", ""),
            "date": payload.get("date", ""),
            "source": payload.get("source", ""),
            "audioFrequencyData": payload.get("audioFrequencyData", ""),
            "dialogs": payload.get("dialogs", []),
            "subjects": payload.get("subjects", []),
        }

        try:
            response = requests.post(config.wild_box_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending data: {e}")
            return {"error": str(e)}


sender = Sender()
