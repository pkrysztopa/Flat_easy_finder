class HtmlGenerator:
    def __init__(self, cursor, data, rows_per_page, page):
        self.cursor = cursor
        self.data = data
        self.rows_per_page = rows_per_page
        self.page = page

    def generate_table(self, columns=None):
        html_data = '<form method="GET" action="/">'
        html_data += '<label for="rows_per_page">Liczba rekordów na stronie:</label>'
        html_data += '<input type="text" id="custom_rows_per_page" name="custom_rows_per_page" placeholder="Wpisz własną wartość" value="{}">'.format(self.rows_per_page)
        html_data += '<input type="submit" value="Zastosuj">'
        html_data += '</form>'

        html_data += '<form method="GET" action="/">'
        html_data += '<label for="column_sort">Sortuj wg kolumny:</label>'
        html_data += '<select id="column_asc" name="col_asc">'
        for desc in self.cursor.description:
            column_name = desc[0]
            selected = 'selected' if columns is not None and column_name in columns else ''
            html_data += '<option value="{}" {}>{}</option>'.format(column_name, selected, column_name)
        html_data += '</select>'

        html_data += '<form method="GET" action="/">'
        html_data += '<table style="border-collapse: collapse; width: 100%;">\n'
        html_data += '<tr style="border: 1px solid black;">'
        for desc in self.cursor.description:
            column_name = desc[0]
            checked = 'checked' if columns is None or column_name in columns else ''
            html_data += '<th style="border: 1px solid black; padding: 5px;">'
            html_data += '<label for="{}"><input type="checkbox" id="{}" name="columns" value="{}" {}> {}</label>'.format(column_name, column_name, column_name, checked, column_name)
            html_data += '</th>'
        html_data += '</tr>\n'

        html_data += '<input type="submit" value="Zastosuj">'
        html_data += '</form>'

        start_index = (self.page - 1) * self.rows_per_page
        end_index = start_index + self.rows_per_page
        for i, row in enumerate(self.data[start_index:end_index]):
            html_data += '<tr style="border: 1px solid black;">'
            for item in row:
                html_data += '<td style="border: 1px solid black; padding: 5px;">{}</td>'.format(item)
            html_data += '</tr>\n'
        html_data += '</table>'

        if self.page > 1:
            prev_page = self.page - 1
            html_data += '<a href="/?page={}"><button>Poprzednia strona</button></a>'.format(prev_page)
        if end_index < len(self.data):
            next_page = self.page + 1
            html_data += '<a href="/?page={}"><button>Następna strona</button></a>'.format(next_page)
        return html_data