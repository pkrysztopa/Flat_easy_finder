from selenium import webdriver
from selenium.webdriver.common.by import By
import os


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
        self.url = (
            f"https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/"
            f"cala-polska?page={self.page_no}&limit=72&by=LATEST&direction=DESC"
        )

    def make_connection(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_driver = os.getcwd() + "\\chromedriver.exe"
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path=chrome_driver
        )
        self.driver.get(self.url)

    def scroll_down(self):
        while True:
            try:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                break
            except:
                pass

    def get_links(self):
        elems = self.driver.find_elements(By.XPATH, "//a[@href]")
        for elem in elems:
            link = elem.get_attribute("href")
            if link.startswith("https://www.otodom.pl/pl/oferta/"):
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
