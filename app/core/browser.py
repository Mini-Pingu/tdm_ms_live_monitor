import time

import undetected_chromedriver as uc

from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from .config import Config


class Browser:
    def __init__(self, headless=True, silent=False):
        self.headless = headless
        self.silent = silent
        self.driver = None
        self.setup_driver()

    def setup_driver(self):
        """配置并启动Chrome浏览器（无头模式）"""
        if self.driver:
            self.close_driver()

        chrome_options = Options()
        chrome_options.binary_location = Config.CHROME_BINARY_PATH

        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        if self.silent:
            chrome_options.add_argument("--mute-audio")

        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        try:
            service = Service(executable_path=Config.BROWSER_DRIVER_PATH)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            print("Chrome driver started successfully.")
        except WebDriverException as e:
            print(f"Error starting Chrome driver: {e}")
            raise

    def start_recording(self):
        if not self.driver:
            print("No driver opened.")
            return False

        try:
            play_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "play-button"))
            )
            play_button.click()
            print("Play button clicked.")

            time.sleep(0.5)
            WebDriverWait(self.driver, 5).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True

        except TimeoutException:
            print("Timed out.")
            return False

        except Exception as e:
            print("An error occurred while starting recording:", e)
            return False

    def close_driver(self):
        if self.driver:
            try:
                self.driver.quit()
                print("Driver closed.")
            except Exception as e:
                print(f"Error closing driver: {e}")
            finally:
                self.driver = None
