from src.tracking.crawler import WebCrawler
from src.tracking.scraper import WebScraper
from src.tracking.transformer import Transformer
from src.tracking.db_handler import DBHandler
import pickle


class FlatEasyFinder:
    def __init__(self):
        self.processor = WebScraper()
        self.transformer = Transformer()
        self.db_handler = DBHandler("houses.db")
        self.crawler = WebCrawler()

    def add_flats(self, page_no):
        self.crawler.scrape_links(page_no)
        self.db_handler.create_table()
        with self.db_handler as db:
            for link in self.crawler.links:
                flat = self.processor.flat
                self.processor.scrap_oto(link)
                flat = self.transformer.transform_oto(flat)
                self.db_handler.save_to_db(flat)

