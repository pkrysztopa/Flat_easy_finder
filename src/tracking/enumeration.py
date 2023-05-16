from enum import Enum

class MagicData(Enum):
    BRAK = "brak"
    ZAPYTAJ = "zapytaj"
    BASE_URL_PT1 = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/cala-polska?page="
    BASE_URL_PT2 = "&limit=72&by=LATEST&direction=DESC"
    STARTS_WITH = "https://www.otodom.pl/pl/oferta/"
    EXAMPLE_LINK = "https://www.otodom.pl/pl/oferta/sprzedam-mieszkanie-w-wodzislawiu-slaskim-ID4kPir.html#"