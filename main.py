from bs4 import BeautifulSoup
import lxml
import requests
from src.tracking.crawler import WebCrawler

web = WebCrawler()
web.get_first_url()
web.make_connection()
web.scroll_down()
web.get_links()
web.close_connection()
web.upload_data()
web.get_next_url()