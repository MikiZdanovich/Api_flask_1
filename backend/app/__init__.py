import os
from flask import Flask
from backend.database.database import configure_engine, metadata
from backend.app.config import config_by_name


def create_app(config_name):
    engine = configure_engine(os.getenv('DATABASE_URL'))
    # engine = configure_engine('postgresql://user:password@db:5432/db_1')
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    metadata.bind = engine
    with app.app_context():
        return app