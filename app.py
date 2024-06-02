from flask import Flask, jsonify, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
PORT = 8080
app = Flask(__name__)




if __name__=="__main__":
    app.run(debug=True, port=PORT)