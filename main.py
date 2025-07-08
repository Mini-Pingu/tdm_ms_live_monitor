import os
import time
import random
import datetime
import schedule

from app.core.config import config
from app.core.sender import Sender
from app.core.audio_fetcher import AudioFetcher
from app.core.post_handler import post_handler
from app.core.logger import logger


class Crawler:
    def __init__(self):
        self.audio_fetcher = AudioFetcher()
        self.sender = Sender()

        if not os.path.exists(config.temp_folder):
            os.makedirs(config.temp_folder)

    def crawl(self):
        start_time = datetime.datetime.now()
        while (
            datetime.datetime.now() - start_time
        ).total_seconds() < config.max_min_per_section * 60:
            logger.info("Starting to crawl TDM live audio...")
            chunk_list = self.audio_fetcher.chunk_list_handler()
            audio_name = self.audio_fetcher.audio_list_handler(chunk_list)
            audio_file = self.audio_fetcher.audio_handler(audio_name)
            logger.info("Crawling TDM live audio file: %s", audio_file)
            random_sleeping_sec = random.randint(3, 5)
            time.sleep(random_sleeping_sec)
            logger.info("Sleeping: %s sec", random_sleeping_sec)

    @staticmethod
    def data_handler():
        post_handler.audio_handler()
        text = post_handler.asr_handler()
        print("text:", text)
        # print(post_handler.llm_handler(text))
        # self.sender.send()


def main():
    crawler = Crawler()
    # crawler.crawl()
    crawler.data_handler()

    # schedule.every().day.at("00:12").do(crawler.crawl)
    #
    # # schedule.every().day.at("08:30").do(crawler.crawl)
    # # schedule.every().day.at("09:00").do(crawler.crawl)
    # # schedule.every().day.at("09:30").do(crawler.crawl)
    # # schedule.every().day.at("10:00").do(crawler.crawl)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


if __name__ == "__main__":
    main()
