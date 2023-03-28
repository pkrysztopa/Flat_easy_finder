from transformer import Transformer
import sqlite3

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

    def add_estate(self, soup, link):
        soup_1 = soup.find_all('div', class_='css-1k2qr23 enb64yk0')
        soup_2 = soup.find_all('div', class_='css-kkaknb enb64yk0')
        soup_3 = soup.find_all('a', class_='css-1in5nid e19r3rnf1')
        row = []

        for record in soup_1:
            data = self.tr.clean_soup(record)
            row.append(data)
        for record in soup_2:
            data = self.tr.clean_soup(record)
            row.append(data)
        for record in soup_3:
            data = record.text.strip()
            row.append(data)

        price = self.tr.price(soup.find('strong', class_='css-1i5yyw0 e1l1avn10'))
        market = row[0]
        advertiser = row[1]
        year_built = self.tr.year_built(row[3])
        estate_type = row[4]
        windows = row[5]
        lift = row[6]
        utilities = row[7]
        security = row[8]
        furnishing = row[9]
        other_info = row[10]
        material = row[11]
        area = self.tr.area(row[12])
        legal_status = row[13]
        rooms = self.tr.rooms(row[14])
        condition = row[15]
        level = row[16]
        balcony = row[17]
        rent = self.tr.rent(row[18])
        parking = row[19]
        heating = row[21]
        province = row[23]

        try:
            city, district, street = self.tr.localisation(row[24], row[25], row[26])
        except IndexError:
            try:
                city, district, street = self.tr.localisation(row[24], row[25])
            except IndexError:
                city, district, street = self.tr.localisation(row[24])

        query = "INSERT INTO Houses(Cena, Powierzchnia, Województwo, Miasto, Osiedle, Ulica, Rynek,\
        Typ_ogłoszeniodawcy, Rok_budowy, Typ_budynku, Okna, Winda, Media, Zabezpieczenia, Wyposażenie,\
        Informacje_dodatkowe, Materiał_budynku, Stan_prawny, Liczba_pokoi, Stan_wykończenia,\
        Piętro, Balkon_taras, Czynsz, Parking, Ogrzewanie, Link)\
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.con.execute(query, (price, area, province, city, district, street, market,
                                 advertiser, year_built, estate_type, windows, lift, utilities, security,
                                 furnishing, other_info, material, legal_status, rooms,
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