from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://www.otodom.pl/pl/oferta/dom-premium-120-m2-w-zabudowie-blizniaczej-wawer-ID4hQm3")

soup = BeautifulSoup(response.text, "html.parser")
soup.find_al