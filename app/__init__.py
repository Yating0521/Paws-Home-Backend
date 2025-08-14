from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')

    # Import and register blueprints
    # from app.routes import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_PUBLIC_URL")
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app