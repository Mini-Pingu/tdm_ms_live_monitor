import time

import undetected_chromedriver as uc

from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Browser:
    def __init__(self, headless=True, silent=False):
        self.headless = headless
        self.silent = silent
        self.driver = None

    def setup_driver(self):
        options = uc.ChromeOptions()
        # options.version_main = 138

        if self.driver:
            self.close_driver()

        if self.headless:
            options.add_argument("--headless=new")

        if self.silent:
            options.add_argument("--mute-audio")

        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        try:
            self.driver = uc.Chrome(
                options=options,
                use_subprocess=False,
                driver_executable_path="/usr/local/bin/chromedriver",
                service_args=["--verbose"],  # 启用详细日志
                service_log_path="chromedriver.log",  # 输出日志到文件
            )
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
