import os
import time
import random
import datetime
import schedule

from app.core.config import config
from app.core.audio_fetcher import audio_fetcher
from app.core.post_handler import post_handler
from app.core.logger import logger
from app.core.sender import sender


class Crawler:
    def __init__(self):
        if not os.path.exists(config.temp_folder):
            os.makedirs(config.temp_folder)

    @staticmethod
    def crawl():
        start_time = datetime.datetime.now()
        logger.info("===================================")
        logger.info("Starting to crawl TDM live audio...")
        while (
            datetime.datetime.now() - start_time
        ).total_seconds() < config.max_min_per_section * 60:
            chunk_list = audio_fetcher.chunk_list_handler()
            audio_name = audio_fetcher.audio_list_handler(chunk_list)
            audio_file = audio_fetcher.audio_handler(audio_name)
            logger.info("Crawling TDM live audio file: %s", audio_file)
            random_sleeping_sec = random.randint(3, 5)
            time.sleep(random_sleeping_sec)
            logger.info("Sleeping: %s sec", random_sleeping_sec)

    @staticmethod
    def data_handler():
        post_handler.audio_handler()
        dialog_text, total_text = post_handler.asr_handler()
        analyzed_text = post_handler.analyze_handler(total_text)
        output = post_handler.output_handler(dialog_text, analyzed_text)
        response = sender.send(output)
        logger.info("Wild Box API response: %s", response)
        logger.info("Data handling completed.")
        logger.info("===================================")


def routine():
    try:
        crawler = Crawler()
        crawler.crawl()
        crawler.data_handler()
    except Exception as e:
        logger.error(f"An error occurred during the routine: {e}", exc_info=True)
    finally:
        for f in os.listdir(config.temp_folder):
            file_path = os.path.join(config.temp_folder, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
        logger.info("Crawling and data handling completed.")
        logger.info("Routine finished and temporary files cleaned up.")
        logger.info("=====================================")


def main():
    logger.info("********************************")
    logger.info("Starting TDM live audio crawler.")
    schedule.every().day.at("08:30").do(routine)
    schedule.every().day.at("09:05").do(routine)
    schedule.every().day.at("09:35").do(routine)
    schedule.every().day.at("10:05").do(routine)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
