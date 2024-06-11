from flask import Blueprint, render_template
import requests

frontend_blueprint = Blueprint('frontend', __name__)

@frontend_blueprint.route('/')
@frontend_blueprint.route('/home')

@frontend_blueprint.route('/home/')
def index():
    builds = requests.get('http://192.168.0.8:5000/api/builds/').json()
    pokemons = requests.get('http://192.168.0.8:5000/api/pokemons/').json()
    #pokemon_dict = {pokemon['id']: pokemon for pokemon in pokemons}
    #pokemon dict but its only owner and pokedex
    
    build_dict = {}

    for i in range(len(builds)):
        id1 = int(builds[i]['pokemon_id_1'])
        try:
            print(pokemons[id1])
            #print(id1)
            print("\n")
        except IndexError as e:
            print(f"Error encontrado en la base de datos, iteracion {i}: indexError {e}")



            
        build_dict[builds[i]['id']] = {
            'owner_id': builds[i]['owner_id'],
            'build_name': builds[i]['build_name'],
            'timestamp': builds[i]['timestamp'],
            'pokemon_id_1': builds[i]['pokemon_id_1']
            #'pokemon_id_2': builds[i]['pokemon_id_2'],
            #'pokemon_id_3': builds[i]['pokemon_id_3'],
            #'pokemon_id_4': builds[i]['pokemon_id_4'],
            #'pokemon_id_5': builds[i]['pokemon_id_5'],
            #'pokemon_id_6': builds[i]['pokemon_id_6']
        }
    
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


@frontend_blueprint.route('/login_register')
def login_register():
    return render_template('login_register.html')