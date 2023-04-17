from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from enumeration import MagicData
import pickle

class WebCrawler:
    def __init__(self):
        self.links = set()
        self.page_no = 1
        self.url = f"{MagicData.BASE_URL_PT1.value}{self.page_no}{MagicData.BASE_URL_PT2.value}"


    def __get_next_url(self):
        self.page_no += 1
        self.url = f"{MagicData.BASE_URL_PT1.value}{self.page_no}{MagicData.BASE_URL_PT2.value}"

    def __make_connection(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_driver = os.getcwd() + "\\chromedriver.exe"
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path=chrome_driver
        )
        self.driver.get(self.url)

    def __scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def __get_links(self):
        elems = self.driver.find_elements(By.XPATH, "//a[@href]")
        for elem in elems:
            link = elem.get_attribute("href")
            if link.startswith(MagicData.STARTS_WITH.value):
                self.links.add(link)

    def __close_connection(self):
        self.driver.quit()

    def scrape_links(self, page_no):
        for i in range(page_no):
            self.__make_connection()
            self.__scroll_down()
            self.__get_links()
            self.__close_connection()
            self.__get_next_url()

    def scrape_links_to_file(self, page_no, file):
        for i in range(page_no):
            self.__make_connection()
            self.__scroll_down()
            self.__get_links()
            self.__close_connection()
            self.__get_next_url()
        with open(file, 'wb') as f:
            pickle.dump(self.links, f)