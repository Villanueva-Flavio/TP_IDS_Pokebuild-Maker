from flask import Blueprint, render_template

frontend_blueprint = Blueprint('frontend', __name__)

@frontend_blueprint.route('/')
def index():
    return render_template('home.html')


@frontend_blueprint.route('/pop-up-test')
def pop_up_test():
    return render_template('pop-up-test.html')

@frontend_blueprint.route('/build_list_container')
def build_list_container():
    # requests de fotos de pokemons
    # llamar a api con las builds y sus pokemons
    lista=[1,2,3,4,5,6,7,8,9] #Quitar lista
    return render_template("build_list_container.html",lista=lista)
