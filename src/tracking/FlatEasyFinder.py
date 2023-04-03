from src.tracking.crawler import WebCrawler
from src.tracking.processor import WebProcessor
from src.tracking.transformer import Transformer
from src.tracking.dbhandler import DBHandler

class FlatEasyFinder:
    def __init__(self):
       self.processor = WebProcessor()
       self.transformer = Transformer()
       self.db_handler = DBHandler('houses.db')
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

finder = FlatEasyFinder()
finder.add_flats(3)





