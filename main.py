from app.core.browser import Browser


class Crawler:
    def __init__(self, url):
        self.url = url
        self.browser = Browser(headless=False, silent=False)

    def crawl(self):
        if self.browser.start_recording():
            print("Crawling...")
        else:
            print("Failed to start recording. Cannot crawl.")


if __name__ == "__main__":
    # Example usage
    target_url = "https://example.com"
    crawler = Crawler(target_url)
    crawler.crawl()
