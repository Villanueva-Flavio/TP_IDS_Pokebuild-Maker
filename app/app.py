from flask import Flask
from api import api_blueprint  # Importa desde api.py
from frontend import frontend_blueprint  # Importa desde frontend.py

app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(frontend_blueprint)

@app.route('/')
def home():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
