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

    database_url = os.getenv("DATABASE_PUBLIC_URL") or os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_PUBLIC_URL or DATABASE_URL is not set!")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    
    db.init_app(app)
    CORS(app)

    # with app.app_context():
    #     db.create_all()
    import app.routes

    return app