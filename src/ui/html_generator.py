from src.tracking.db_handler import DBHandler
from os.path import join, dirname, abspath
db_path = join(dirname(dirname(abspath(__file__))), 'tracking/houses.db')

class HtmlGenerator:
    def __init__(self, cursor, data, rows_per_page):
        self.cursor = cursor
        self.data = data
        self.rows_per_page = rows_per_page

    def generate_table(self):
        html_data = '<form method="GET" action="/">'
        html_data += '<label for="rows_per_page">Liczba rekordów na stronie:</label>'
        html_data += '<input type="text" id="custom_rows_per_page" name="custom_rows_per_page" placeholder="Wpisz własną wartość" value="{}">'.format(self.rows_per_page)
        html_data += '<input type="submit" value="Zastosuj">'
        html_data += '</form>'

        html_data += '<table style="border-collapse: collapse; width: 100%;">\n'
        html_data += '<tr style="border: 1px solid black;">' + ''.join(['<th style="border: 1px solid black; padding: 5px;">{}</th>'.format(desc[0]) for desc in self.cursor.description]) + '</tr>\n'
        for i, row in enumerate(self.data):
            if i >= self.rows_per_page:
                break
            html_data += '<tr style="border: 1px solid black;">'
            for item in row:
                html_data += '<td style="border: 1px solid black; padding: 5px;">{}</td>'.format(item)
            html_data += '</tr>\n'
        html_data += '</table>'
        return html_data