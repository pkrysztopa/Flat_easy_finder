from flask import Flask, render_template, request
from src.ui.html_generator import HtmlGenerator
from src.tracking.db_handler import DBHandler
from os.path import join, dirname, abspath
from src.tracking.flat_easy_finder import FlatEasyFinder

db_path = join(dirname(dirname(abspath(__file__))), 'tracking/houses.db')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    db = DBHandler(db_path)
    rows_per_page = int(request.args.get('rows_per_page',10))
    page = int(request.args.get('page', 1))
    columns = request.args.getlist('columns')
    col_asc = request.args.get('col_asc')
    sort_order = request.args.get('sort_order')
    filter_column = request.args.get('filter_column')
    filter_value = request.args.get('filter_value')
    data = db.fetch_data(columns, col_asc, sort_order, filter_column, filter_value)
    html_generator = HtmlGenerator(db.cursor, data, rows_per_page, page)
    html_data = html_generator.generate_table(sort_order, columns, col_asc, filter_column)
    if request.method == 'POST':
        page_no = int(request.form['page_no'])
        flat_finder = FlatEasyFinder()
        flat_finder.add_flats(page_no)
    return render_template('index.html', html_data=html_data)
