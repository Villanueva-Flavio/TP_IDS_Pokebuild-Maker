from flask import Flask
from api import api_blueprint  # Importa desde api.py

app = Flask(__name__)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
