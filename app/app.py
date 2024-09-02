from flask import Flask
from app.main import main  # Importación absoluta

app = Flask(__name__, static_folder='app/static')
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
