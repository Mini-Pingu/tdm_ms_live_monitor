from app.core.sender import Sender


class Crawler:
    def __init__(self):
        self.sender = Sender()

    def crawl(self):
        pass


if __name__ == "__main__":
    # Example usage
    crawler = Crawler()
    crawler.crawl()
