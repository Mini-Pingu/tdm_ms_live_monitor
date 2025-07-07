# import time
# from app.core.browser import Browser
import json
from app.core.sender import Sender


class Crawler:
    def __init__(self):
        # self.browser = Browser(headless=False, silent=False)
        self.sender = Sender()

    def crawl(self):
        data = {
            "title": "Title",
            "sumarization": "sumarization",
            "date": "2025-07-08 11:00:00",
            "source": "MS",
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

        # self.browser.setup_driver()
        # self.browser.driver.get(self.url)
        # time.sleep(30)
        # self.browser.close_driver()


if __name__ == "__main__":
    # Example usage
    crawler = Crawler()
    crawler.crawl()
