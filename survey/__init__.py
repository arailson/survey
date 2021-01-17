import logging
from flask import Flask
from survey.config import Config
from flask_sqlalchemy import SQLAlchemy

__version__ = "0.1.0"

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logging.basicConfig(
    handlers=[console],
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from survey.routes import main

    app.register_blueprint(main)

    return app