import unittest
from src.tracking.transformer import Transformer
from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from src.tracking.flat import Flat


class TestTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = Transformer()

    def test__strip_letters(self):
        result = self.transformer._Transformer__strip_letters(None)
        assert result == None
        result = self.transformer._Transformer__strip_letters('')
        assert result == None
        result = self.transformer._Transformer__strip_letters('abc')
        assert result == None
        result = self.transformer._Transformer__strip_letters('123.45')
        assert result == '123.45'
        result = self.transformer._Transformer__strip_letters('1,234.56')
        assert result == '1,234.56'
        result = self.transformer._Transformer__strip_letters('1a2b3c.4d5e')
        assert result == '123.45'

    def test_clean_price(self):
        expr = MagicMock(text="10 000.00 PLN")
        result = self.transformer.clean_price(expr)
        assert result == 10000

    def test_clean_integer(self):
        expr = BeautifulSoup("<div>/*5 piętro*/</div>")
        result = self.transformer.clean_integer(expr)
        assert result == 5

    def test_clean_float(self):
        expr = BeautifulSoup("<div>/*50,2 m*/</div>")
        result = self.transformer.clean_float(expr)
        assert result == 50.2

    def test_clean_string(self):
        expr = BeautifulSoup("<div>/*Zapytaj</div>")
        result = self.transformer.clean_string(expr)
        assert result is None

    def test_localize(self):
        loc_list = ["Adres", "Mazowieckie", "Warszawa", "Śródmieście", "ul. Marszałkowska"]
        city, district, street, province = self.transformer.localize(loc_list)
        assert city == "Warszawa"
        assert district == "Śródmieście"
        assert street == "ul. Marszałkowska"
        assert province == "Mazowieckie"

    def test_transform_oto(self):
        flat = Flat()
        flat.price = MagicMock(text="10 000,00 PLN")
        flat.market = BeautifulSoup("<div>/* pierwotny /*</div>")
        flat.advertiser = BeautifulSoup("<div>/* agencja /*</div>")
        flat.year_built = BeautifulSoup("<div>/* 2000 /*</div>")
        flat.estate_type = BeautifulSoup("<div>/* mieszkanie /*</div>")
        flat.windows = BeautifulSoup("<div>/* plastikowe /*</div>")
        flat.lift = BeautifulSoup("<div>/* tak /*</div>")
        flat.utilities = BeautifulSoup("<div>/*prąd, gaz, woda, kanalizacja /*</div>")
        flat.security = BeautifulSoup("<div>/* drzwi antywłamaniowe /*</div>")
        flat.furnishing = BeautifulSoup("<div>/* umeblowane /*</div>")
        flat.other_info = BeautifulSoup("<div>/* blisko metra /*</div>")
        flat.material = BeautifulSoup("<div>/* cegła /*</div>")
        flat.area = BeautifulSoup("<div>/* 60,00 m² /*</div>")
        flat.legal_status = BeautifulSoup("<div>/* własność /*</div>")
        flat.rooms = BeautifulSoup("<div>/* 2 pokoje /*</div>")
        flat.condition = BeautifulSoup("<div>/* do odświeżenia /*</div>")
        flat.level = BeautifulSoup("<div>/* 2/4 /*</div>")
        flat.balcony = BeautifulSoup("<div>/* nie /*</div>")
        flat.rent = BeautifulSoup("<div>/* 850,30 zł /*</div>")
        flat.parking = BeautifulSoup("<div>/* garaż /*</div>")
        flat.heating = BeautifulSoup("<div>/* miejskie /*</div>")
        flat.loc_list = ["Adres", "Mazowieckie", "Warszawa", "Śródmieście", "ul. Marszałkowska"]
        self.transformer.transform_oto(flat)
        assert flat.price == 10000
        assert flat.market == 'pierwotny'
        assert flat.advertiser == 'agencja'
        assert flat.year_built == 2000
        assert flat.estate_type == 'mieszkanie'
        assert flat.windows == 'plastikowe'
        assert flat.lift == 'tak'
        assert flat.utilities == 'prąd, gaz, woda, kanalizacja'
        assert flat.security == 'drzwi antywłamaniowe'
        assert flat.furnishing == 'umeblowane'
        assert flat.other_info == 'blisko metra'
        assert flat.material == 'cegła'
        assert flat.area == 60
        assert flat.legal_status == 'własność'
        assert flat.rooms == 2
        assert flat.condition == 'do odświeżenia'
        assert flat.level == '2/4'
        assert flat.balcony == 'nie'
        assert flat.rent == 850.30
        assert flat.parking == 'garaż'
        assert flat.heating == 'miejskie'
        assert flat.city == "Warszawa"
        assert flat.district == "Śródmieście"
        assert flat.street == "ul. Marszałkowska"
        assert flat.province == "Mazowieckie"
