from flask import Flask
from flask_session import Session
from api import api_blueprint
from frontend import frontend_blueprint
from flask_cors import CORS

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'Secret key test'
Session(app)
CORS(app)

app.register_blueprint(api_blueprint)
app.register_blueprint(frontend_blueprint)