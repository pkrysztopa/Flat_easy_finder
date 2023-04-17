import sqlite3


class DBHandler:
    def __init__(self, path):
        self.path = path
        self.con = sqlite3.connect(self.path)
        self.cursor = self.con.cursor()

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
        Link TEXT UNIQUE);"

        self.con.execute(query)

    def save_to_db(self, flat):

        query = "INSERT OR IGNORE INTO Houses(Cena, Powierzchnia, Województwo, Miasto, Osiedle, Ulica, Rynek,\
        Typ_ogłoszeniodawcy, Rok_budowy, Typ_budynku, Okna, Winda, Media, Zabezpieczenia, Wyposażenie,\
        Informacje_dodatkowe, Materiał_budynku, Stan_prawny, Liczba_pokoi, Stan_wykończenia,\
        Piętro, Balkon_taras, Czynsz, Parking, Ogrzewanie, Link)\
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.con.execute(
            query,
            (
                flat.price,
                flat.area,
                flat.province,
                flat.city,
                flat.district,
                flat.street,
                flat.market,
                flat.advertiser,
                flat.year_built,
                flat.estate_type,
                flat.windows,
                flat.lift,
                flat.utilities,
                flat.security,
                flat.furnishing,
                flat.other_info,
                flat.material,
                flat.legal_status,
                flat.rooms,
                flat.condition,
                flat.level,
                flat.balcony,
                flat.rent,
                flat.parking,
                flat.heating,
                flat.link,
            ),
        )

    def fetch_all_data(self):
        query = "SELECT * FROM Houses"
        results = self.cursor.execute(query).fetchall()
        return results

    def fetch_data(self, columns=None, col_asc=None, asc=True):
        if not columns:
            query = "SELECT * FROM Houses"
        else:
            column_names = ', '.join(columns)
            query = f"SELECT {column_names} FROM Houses"
        if col_asc is not None:
            sort_order = "ASC" if asc else "DESC"
            query += f" ORDER BY {col_asc} {sort_order}"
        results = self.cursor.execute(query).fetchall()
        return results

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()
