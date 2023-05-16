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

        attributes = [
            'loc_list', 'price', 'year_built', 'link', 'market', 'advertiser', 'estate_type',
            'windows', 'lift', 'utilities', 'security', 'furnishing', 'other_info', 'material',
            'area', 'legal_status', 'rooms', 'condition', 'level', 'balcony', 'rent', 'parking', 'heating'
        ]

        for attribute in attributes:
            assert getattr(self.scraper.flat, attribute) is not None
















