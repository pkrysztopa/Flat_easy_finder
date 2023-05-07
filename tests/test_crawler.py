import unittest
from unittest.mock import MagicMock
from src.tracking.crawler import WebCrawler
from src.tracking.enumeration import MagicData
import pickle
from selenium import webdriver


class TestWebCrawler(unittest.TestCase):

    def setUp(self):
        self.web_crawler = WebCrawler()

    def tearDown(self):
        pass

    def test__get_next_url(self):
        self.web_crawler.page_no = 1
        self.web_crawler._WebCrawler__get_next_url()
        self.assertEqual(self.web_crawler.url, f'{MagicData.BASE_URL_PT1.value}2{MagicData.BASE_URL_PT2.value}')

    def test__make_connection(self):
        webdriver.Chrome = MagicMock()
        self.web_crawler.url = 'www.example.com'
        self.web_crawler._WebCrawler__make_connection()
        self.web_crawler.driver.get.assert_called_with('www.example.com')

    def test__scroll_down(self):
        self.web_crawler._WebCrawler__make_connection()
        self.web_crawler.driver.execute_script = MagicMock()
        self.web_crawler._WebCrawler__scroll_down()
        self.web_crawler.driver.execute_script.assert_called_once_with(
            "window.scrollTo(0, document.body.scrollHeight);")

    def test__get_links(self):
        self.web_crawler._WebCrawler__make_connection()
        self.web_crawler._WebCrawler__get_links()
        self.assertTrue(self.web_crawler.links)

    def test__close_connection(self):
        webdriver.Chrome = MagicMock()
        self.web_crawler._WebCrawler__make_connection()
        self.web_crawler._WebCrawler__close_connection()
        self.web_crawler.driver.quit.assert_called_once()

    def test_scrape_links(self):
        self.web_crawler.scrape_links(1)
        self.assertTrue(self.web_crawler.links)

    def test_scrape_links_to_file(self):
        file = "test_links.db"
        self.web_crawler.scrape_links_to_file(1, file)
        with open(file, 'rb') as f:
            links = pickle.load(f)
        self.assertTrue(links)

