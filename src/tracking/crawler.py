from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from scrapper import Estates_DB

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/cala-polska?page=1&limit=72&by=LATEST&direction=DESC'

links = set()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920x8000")
chrome_options.add_argument("--headless")
chrome_driver = os.getcwd() + "\\chromedriver.exe"  # CHANGE THIS IF NOT SAME FOLDER
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
driver.get(url)
while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        break
    except:
        pass

elems = driver.find_elements(By.XPATH,"//a[@href]")
for elem in elems:
    link = elem.get_attribute("href")
    if link.startswith('https://www.otodom.pl/pl/oferta/'):
        links.add(link)

driver.quit()

with Estates_DB('houses.db') as db:
    db.create_table()
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "lxml")
        db.add_estate(soup, link)