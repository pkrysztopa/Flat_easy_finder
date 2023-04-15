import requests
from bs4 import BeautifulSoup
from src.tracking.flat import Flat
from decorators import timethis


class WebScraper:
    def __init__(self):
        self.soup = None
        self.flat = Flat()

    def create_soup(self, link):
        response = requests.get(link)
        self.soup = BeautifulSoup(response.text, "lxml")


    def scrap_oto(self, link):

        self.create_soup(link)

        localisation = self.soup.find_all("a", class_="css-1in5nid e19r3rnf1")
        self.flat.loc_list.clear()
        for record in localisation:
            self.flat.loc_list.append(record.text.strip())

        self.flat.price = self.soup.find(attrs={"aria-label": "Cena"})
        self.flat.market = self.soup.find(attrs={"aria-label": "Rynek"})
        self.flat.advertiser = self.soup.find(
            attrs={"aria-label": "Typ ogłoszeniodawcy"}
        )
        self.flat.year_built = self.soup.find(attrs={"aria-label": "Rok budowy"})
        self.flat.estate_type = self.soup.find(attrs={"aria-label": "Rodzaj zabudowy"})
        self.flat.windows = self.soup.find(attrs={"aria-label": "Okna"})
        self.flat.lift = self.soup.find(attrs={"aria-label": "Winda"})
        self.flat.utilities = self.soup.find(attrs={"aria-label": "Media"})
        self.flat.security = self.soup.find(attrs={"aria-label": "Zabezpieczenia"})
        self.flat.furnishing = self.soup.find(attrs={"aria-label": "Wyposażenie"})
        self.flat.other_info = self.soup.find(
            attrs={"aria-label": "Informacje dodatkowe"}
        )
        self.flat.material = self.soup.find(attrs={"aria-label": "Materiał budynku"})
        self.flat.area = self.soup.find(attrs={"aria-label": "Powierzchnia"})
        self.flat.legal_status = self.soup.find(attrs={"aria-label": "Forma własności"})
        self.flat.rooms = self.soup.find(attrs={"aria-label": "Liczba pokoi"})
        self.flat.condition = self.soup.find(attrs={"aria-label": "Stan wykończenia"})
        self.flat.level = self.soup.find(attrs={"aria-label": "Piętro"})
        self.flat.balcony = self.soup.find(
            attrs={"aria-label": "Balkon / ogród / taras"}
        )
        self.flat.rent = self.soup.find(attrs={"aria-label": "Czynsz"})
        self.flat.parking = self.soup.find(attrs={"aria-label": "Miejsce parkingowe"})
        self.flat.heating = self.soup.find(attrs={"aria-label": "Ogrzewanie"})
        self.flat.link = link
