import csv
from flask import Flask, render_template, request
from src.ui.html_generator import HtmlGenerator
from src.tracking.db_handler import DBHandler
from os.path import join, dirname, abspath
from src.tracking.flat_easy_finder import FlatEasyFinder

db_path = join(dirname(dirname(abspath(__file__))), 'tracking/houses.db')

app = Flask(__name__)

stored_settings = {
    'rows_per_page': 10,
    'columns': [],
    'col_asc': None,
    'sort_order': None,
    'filter_column': None,
    'filter_value': None
}


@app.route('/', methods=['GET', 'POST'])
def index():
    global stored_settings

    db = DBHandler(db_path)

    rows_per_page = int(request.args.get('rows_per_page', stored_settings['rows_per_page']))
    page = int(request.args.get('page', 1))
    columns = request.args.getlist('columns') or stored_settings['columns']
    col_asc = request.args.get('col_asc') or stored_settings['col_asc']
    sort_order = request.args.get('sort_order') or stored_settings['sort_order']
    filter_column = request.args.get('filter_column') or stored_settings['filter_column']
    filter_value = request.args.get('filter_value') or stored_settings['filter_value']

    stored_settings['rows_per_page'] = rows_per_page
    stored_settings['columns'] = columns
    stored_settings['col_asc'] = col_asc
    stored_settings['sort_order'] = sort_order
    stored_settings['filter_column'] = filter_column
    stored_settings['filter_value'] = filter_value

    data = db.fetch_data(columns, col_asc, sort_order, filter_column, filter_value)
    html_generator = HtmlGenerator(db.cursor, data, rows_per_page, page)
    html_data = html_generator.generate_table(columns)

    if request.method == 'POST':
        page_no = int(request.form['page_no'])
        flat_finder = FlatEasyFinder()
        flat_finder.add_flats(page_no)
    elif request.method == 'GET' and 'save_csv' in request.args:
        save_data_to_csv(data)

    return render_template('index.html', html_data=html_data)


def save_data_to_csv(data):
    file_path = join(dirname(dirname(abspath(__file__))), 'data.csv')
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
