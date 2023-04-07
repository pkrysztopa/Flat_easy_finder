from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5 ### 0

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///src.tracking.houses.db'
    db.init_app(app)

    app.debug = True

    from .main import show_table
    app.register_blueprint(show_table)

    return app