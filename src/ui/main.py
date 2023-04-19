from flask import Flask, render_template, redirect, url_for, Blueprint, request, session
from src.ui.html_generator import HtmlGenerator
from src.tracking.db_handler import DBHandler
from os.path import join, dirname, abspath

db_path = join(dirname(dirname(abspath(__file__))), 'tracking/houses.db')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    db = DBHandler(db_path)
    #request.method == 'GET'
    rows_per_page = int(request.args.get('rows_per_page',10))
    page = int(request.args.get('page', 1))
    columns = request.args.getlist('columns')
    col_asc = request.args.get('col_asc')
    data = db.fetch_data(columns, col_asc)
    html_generator = HtmlGenerator(db.cursor, data, rows_per_page, page)
    html_data = html_generator.generate_table(columns)
    return render_template('index.html', html_data=html_data)
   #data = db.fetch_all_data()
   #html_generator = HtmlGenerator(db.cursor, data, 10, 1)
   #html_data = html_generator.generate_table()
   #return render_template('index.html', html_data=html_data)