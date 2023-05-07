import unittest
from src.ui.html_generator import HtmlGenerator

class TestHtmlGenerator(unittest.TestCase):

    def setUp(self):
        cursor = [('id', 'int'), ('Cena', 'number')]
        data = [[1, 100000], [2, 300000], [3, 405434], [4, 3512345]]
        rows_per_page = 10
        page = 1
        self.generator = HtmlGenerator(cursor, data, rows_per_page, page)

    # TODO: test for generate_table
    def test_html_generator(self):

        table_html = self.generator.generate_table(columns=['id', 'Cena'])
        assert 'Liczba rekordów na stronie:' in table_html
        assert 'wg kolumny:' in table_html
        assert 'checked' in table_html
        assert 'selected' in table_html
        assert '<table style="border-collapse: collapse; width: 100%;">' in table_html
        assert '<td style="border: 1px solid black; padding: 5px;">1</td>' in table_html
        assert '<td style="border: 1px solid black; padding: 5px;">John</td>' in table_html
        assert '<tr style="border: 1px solid black;">' in table_html
        assert '<th style="border: 1px solid black; padding: 5px;">' in table_html

        assert '<input type="submit" value="Poprzednia strona">' in table_html
        assert '<input type="submit" value="Następna strona">' in table_html
