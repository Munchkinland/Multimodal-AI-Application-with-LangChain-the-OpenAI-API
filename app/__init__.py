from flask import Flask
from .main import main

def create_app():
    app = Flask(__name__, static_folder='static')

    # Registro de Blueprints
    app.register_blueprint(main)

    return app