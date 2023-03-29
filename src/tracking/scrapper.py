from src.tracking.transformer import Transformer
import sqlite3
import requests
from bs4 import BeautifulSoup


class Estates_DB:

    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.tr = Transformer()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Houses(\
        id INTEGER PRIMARY KEY,\
        Cena NUMERIC,\
        Powierzchnia NUMERIC,\
        Województwo TEXT,\
        Miasto TEXT,\
        Osiedle TEXT,\
        Ulica TEXT,\
        Rynek TEXT,\
        Typ_ogłoszeniodawcy TEXT,\
        Rok_budowy NUMERIC,\
        Typ_budynku TEXT,\
        Okna TEXT,\
        Winda TEXT,\
        Media TEXT,\
        Zabezpieczenia TEXT,\
        Wyposażenie TEXT,\
        Informacje_dodatkowe TEXT,\
        Materiał_budynku TEXT,\
        Stan_prawny TEXT,\
        Liczba_pokoi NUMERIC,\
        Stan_wykończenia TEXT,\
        Piętro TEXT,\
        Balkon_taras TEXT,\
        Czynsz NUMERIC,\
        Parking TEXT,\
        Ogrzewanie TEXT,\
        Link TEXT);"

        self.con.execute(query)

    def create_soup(self, link):
        response = requests.get(link)
        self.soup = BeautifulSoup(response.text, "lxml")

    def add_estate(self, link):
        self.create_soup(link)
        soup_3 = self.soup.find_all('a', class_='css-1in5nid e19r3rnf1')
        row = []

        for record in soup_3:
            data = record.text.strip()
            row.append(data)

        price = self.tr.price(self.soup.find(attrs={"aria-label": "Cena"}))
        market = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Rynek"}))
        advertiser = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Typ ogłoszeniodawcy"}))
        year_built = self.tr.year_built(self.tr.clean_text(self.soup.find(attrs={"aria-label": "Rok budowy"})))
        estate_type = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Rodzaj zabudowy"}))
        windows = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Okna"}))
        lift = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Winda"}))
        utilities = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Media"}))
        security = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Zabezpieczenia"}))
        furnishing = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Wyposażenie"}))
        other_info = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Informacje dodatkowe"}))
        material = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Materiał budynku"}))
        area = self.tr.area(self.tr.clean_text(self.soup.find(attrs={"aria-label": "Powierzchnia"})))
        legal_status = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Forma własności"}))
        rooms = self.tr.rooms(self.tr.clean_text(self.soup.find(attrs={"aria-label": "Liczba pokoi"})))
        condition = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Stan wykończenia"}))
        level = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Piętro"}))
        balcony = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Balkon / ogród / taras"}))
        rent = self.tr.rent(self.tr.clean_text(self.soup.find(attrs={"aria-label": "Czynsz"})))
        parking = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Miejsce parkingowey"}))
        heating = self.tr.clean_text(self.soup.find(attrs={"aria-label": "Ogrzewanie"}))
        province = row[1]
        try:
            city, district, street = self.tr.localisation(row[2], row[3], row[4])
        except IndexError:
            try:
                city, district, street = self.tr.localisation(row[2], row[3])
            except IndexError:
                city, district, street = self.tr.localisation(row[2])

        query = "INSERT INTO Houses(Cena, Powierzchnia, Województwo, Miasto, Osiedle, Ulica, Rynek,\
        Typ_ogłoszeniodawcy, Rok_budowy, Typ_budynku, Okna, Winda, Media, Zabezpieczenia, Wyposażenie,\
        Informacje_dodatkowe, Materiał_budynku, Stan_prawny, Liczba_pokoi, Stan_wykończenia,\
        Piętro, Balkon_taras, Czynsz, Parking, Ogrzewanie, Link)\
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.con.execute(query, (price, area, province, city, district, street, market, \
                                 advertiser, year_built, estate_type, windows, lift, utilities, security, \
                                 furnishing, other_info, material, legal_status, rooms, \
                                 condition, level, balcony, rent, parking, heating, link))

    def show_houses(self):
        query = "SELECT * FROM Houses"
        results = self.con.execute(query).fetchall()
        print(results)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()