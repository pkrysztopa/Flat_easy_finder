#from src.tracking.crawler import WebCrawler
#from src.tracking.processor import WebProcessor
#
#class WebScraper:
#    def __init__(self):
#        self.web_crawler = WebCrawler()
#        self.web_processor = WebProcessor()
#        self.links = self.web_crawler.links
#
#    def scrape_links(self, page_no):
#        for i in range(page_no):
#            self.web_crawler.make_connection()
#            self.web_crawler.scroll_down()
#            self.web_crawler.get_links()
#            self.web_crawler.close_connection()

    #def scrape_links_all(self):
    #    while
    #        self.web_crawler.make_connection()
    #        self.web_crawler.scroll_down()
    #        self.web_crawler.get_links()
    #        self.web_crawler.close_connection()





scrap = WebScraper()
scrap.scrape(2)
print(scrap.links)

