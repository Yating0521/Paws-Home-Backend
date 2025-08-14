from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # database_url = os.getenv("DATABASE_URL")
    # if not database_url:
    #     raise ValueError("DATABASE_URL is not set!")

    # app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('postgresql://'):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgresql://', 'postgresql+psycopg2://', 1)
    
    db.init_app(app)
    CORS(app)

    # with app.app_context():
    #     db.create_all()
    import app.routes

    return app