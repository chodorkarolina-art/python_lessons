from flask import Flask

from app.db import db
from config import Config
from .routes import BLUEPRINTS

# Import modeli jest konieczny, aby db.create_all() wykryło tabele
from .models import Room, Booking, Equipment, User, Notification


def create_app():
    app = Flask(__name__)

    # lesson18_task1
    app.config.from_object(Config)

    db.init_app(app)

    # Rejestracja wszystkich blueprintów i tras
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
