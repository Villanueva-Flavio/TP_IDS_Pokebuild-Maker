from flask import Blueprint, render_template, request
import requests

frontend_blueprint = Blueprint('frontend', __name__)

@frontend_blueprint.route('/')
def index():
    return render_template('home.html')


@frontend_blueprint.route('/pop-up-test')
def pop_up_test():
    return render_template('pop-up-test.html')

@frontend_blueprint.route('/formulario_añadir_pokemon', methods=["POST", "GET"]) #Hasta que este el POST endpoint de pokemon, tiene esto.
def formulario_añadir_pokemon():
    if request.method == "POST":
        return render_template("home.html")  
    return render_template("formulario_añadir_pokemon.html")

