from app.core.sender import Sender
from app.core.utils import Utils


class Crawler:
    def __init__(self):
        self.sender = Sender()
        self.utils = Utils()

    def crawl(self):
        audio_path = "./data/demo.mp3"
        audio_base64 = self.utils.convert_audio_base64(audio_path)
        data = {
            "title": "Title",
            "sumarization": "sumarization",
            "date": "2025-07-08 11:00:00",
            "source": "MS",
            "audioFrequencyData": audio_base64,
            "dialogs": [
                {"timeStr": "00:10", "content": "content1"},
                {"timeStr": "00:20", "content": "content2"},
            ],
            "subjects": [
                {"title": "tiele1", "content": "subject1"},
                {"title": "tiele2", "content": "subject2"},
            ],
        }
        print(self.sender.send(data))


if __name__ == "__main__":
    # Example usage
    crawler = Crawler()
    crawler.crawl()
