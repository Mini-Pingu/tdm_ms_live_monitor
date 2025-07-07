import requests
from app.core.config import Config


class Sender:
    def __init__(self):
        self.wild_box_url = Config.wild_box_url
        print(self.wild_box_url)

    def send(self, data):
        """
        Sends data to the Wild Box API.

        :param data: The data to be sent.
        :return: Response from the API.
        """

        try:
            response = requests.post(self.wild_box_url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending data: {e}")
            return None
