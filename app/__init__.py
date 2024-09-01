import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    # Acceder a la clave secreta desde las variables de entorno
    app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'clave_por_defecto')  # Usa una clave segura en producción

    # Importar blueprints y registrar rutas
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
