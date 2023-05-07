import unittest
from unittest.mock import MagicMock
from src.tracking.scraper import WebScraper
from src.tracking.enumeration import MagicData

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraper()

    def test_create_soup(self):
        link = "http://example.com"
        self.scraper.create_soup = MagicMock()
        self.scraper.create_soup(link)
        self.scraper.create_soup.assert_called_once_with(link)

    def test_scrap_oto(self):
        link = MagicData.EXAMPLE_LINK.value
        self.scraper.scrap_oto(link)
        assert self.scraper.flat.loc_list is not None
        assert self.scraper.flat.price is not None
        assert self.scraper.flat.year_built is not None
        assert self.scraper.flat.link is not None
        assert self.scraper.flat.market is not None
        assert self.scraper.flat.advertiser is not None
        assert self.scraper.flat.estate_type is not None
        assert self.scraper.flat.windows is not None
        assert self.scraper.flat.lift is not None
        assert self.scraper.flat.utilities is not None
        assert self.scraper.flat.security is not None
        assert self.scraper.flat.furnishing is not None
        assert self.scraper.flat.other_info is not None
        assert self.scraper.flat.material is not None
        assert self.scraper.flat.area is not None
        assert self.scraper.flat.legal_status is not None
        assert self.scraper.flat.rooms is not None
        assert self.scraper.flat.condition is not None
        assert self.scraper.flat.level is not None
        assert self.scraper.flat.balcony is not None
        assert self.scraper.flat.rent is not None
        assert self.scraper.flat.parking is not None
        assert self.scraper.flat.heating is not None
















