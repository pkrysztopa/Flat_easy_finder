from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from enumeration import MagicData

class WebCrawler:
    def __init__(self):
        self.links = set()
        self.page_no = 1
        self.url = (
            f"https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/"
            f"cala-polska?page={self.page_no}&limit=72&by=LATEST&direction=DESC"
        )

    def get_next_url(self):
        self.page_no += 1
        self.url = f"{MagicData.BASE_URL_PT1.value}{self.page_no}{MagicData.BASE_URL_PT2.value}"

    def make_connection(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_driver = os.getcwd() + "\\chromedriver.exe"
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path=chrome_driver
        )
        self.driver.get(self.url)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_links(self):
        elems = self.driver.find_elements(By.XPATH, "//a[@href]")
        for elem in elems:
            link = elem.get_attribute("href")
            if link.startswith(MagicData.STARTS_WITH):
                self.links.add(link)

    def close_connection(self):
        self.driver.quit()

    def scrape_links(self, page_no):
        for i in range(page_no):
            self.make_connection()
            self.scroll_down()
            self.get_links()
            self.close_connection()
            self.get_next_url()
