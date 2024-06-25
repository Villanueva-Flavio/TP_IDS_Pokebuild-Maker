from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify, Blueprint, request
from sqlalchemy import create_engine, text
import os, requests
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

POKEMONS_ROUTE = '/api/pokemons/'
POKEMONS_QUERY = "SELECT * FROM POKEMON"
POKEMON_ID_ROUTE = '/api/pokemon/<pokemon_id>/'
POKEMON_ID_QUERY = "SELECT * FROM POKEMON WHERE ID = "

BUILDS_ROUTE = '/api/builds/'
BUILDS_QUERY = "SELECT * FROM BUILDS"
BUILD_ID_ROUTE = '/api/build/<build_id>/'
BUILD_ID_QUERY = "SELECT * FROM BUILDS WHERE ID = "

USERS_ROUTE = '/api/users_profiles/'
USERS_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u;"
USER_ID_ROUTE = '/api/user_profile/<user_id>/'
USER_ID_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u WHERE id = "

USER_ID_POKEMONS_ROUTE='/api/pokemons_by_user/<owner_id>'
USER_ID_POKEMONS_QUERY= "SELECT id, pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4 FROM POKEMON WHERE owner_id ="

api_blueprint = Blueprint('api', __name__)
db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# GET endpoint for POKEMONS
@api_blueprint.route(POKEMONS_ROUTE, methods=['GET'])
def get_pokemons():
    return get_data(POKEMONS_QUERY)

# GET endpoint for POKEMON by ID
@api_blueprint.route(POKEMON_ID_ROUTE, methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    return get_data(POKEMON_ID_QUERY + pokemon_id)

# GET endpoint for BUILDS
@api_blueprint.route(BUILDS_ROUTE, methods=['GET'])
def get_builds():
    return get_data(BUILDS_QUERY)

# GET endpoint for BUILD by ID
@api_blueprint.route(BUILD_ID_ROUTE, methods=['GET'])
def get_build_by_id(build_id):
    return get_data(BUILD_ID_QUERY + build_id)

# GET endpoint for USERS
@api_blueprint.route(USERS_ROUTE, methods=['GET'])
def get_users_profiles():
    return get_data(USERS_QUERY)

# GET endpoint for USER by ID
@api_blueprint.route(USER_ID_ROUTE, methods=['GET'])
def get_user_profile(user_id):
    return get_data(USER_ID_QUERY + user_id)

# GET endpoint for HOME
@api_blueprint.route('/api', methods=['GET'])
def api_home():
    endpoints = {
        "pokemons": "/api/pokemons",
        "builds": "/api/builds",
        "users_profiles": "/api/users_profiles"
    }
    return jsonify(endpoints)
# GET endpoints for Pokemons by owner_id
@api_blueprint.route(USER_ID_POKEMONS_ROUTE, methods=['GET'])
def get_pokemons_by_user(owner_id):
    return get_data(USER_ID_POKEMONS_QUERY + owner_id)

def get_data(query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            data = []
            for row in result:
                data_dict = dict(row)
                data.append(data_dict)

        if len(data) == 1:
            return jsonify(data[0])
        else:
            return jsonify(data)
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})
    
@api_blueprint.route('/api/types/<pokemon_id>/', methods=['GET'])
def get_pokemon_types(pokemon_id):
    pokemon_id = pokemon_id.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        types = data['types']
        pokemon_type = set()
        good_against = set()
        bad_against = set()

        for slot in types:
            pokemon_type.add(slot['type']['name'])
            coverage = slot['type']['url']
            coverage_response = requests.get(coverage)

            if coverage_response.status_code == 200:
                types_data = coverage_response.json()

                for damage_from in types_data['damage_relations']['double_damage_from']:
                    bad_against.add(damage_from['name'])
                for damage_to in types_data['damage_relations']['double_damage_to']:
                    good_against.add(damage_to['name'])

        return jsonify({
            'pokemon_type': list(pokemon_type),
            'good_against': list(good_against),
            'bad_against': list(bad_against)
        })
    
    else:
        return jsonify({'error': 'Pokemon not found'}), 400

@api_blueprint.route('/api/moves/<pokemon_id>', methods=['GET'])
def get_pokemon_moves(pokemon_id):
    pokemon_id = pokemon_id.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        moves = [move['move']['name'] for move in data['moves']]
        return jsonify({'moves': moves})
    else:
        return jsonify({'error': 'Pokemon not found'}), 404

@api_blueprint.route('/api/get_all_pokemons', methods=['GET'])
def get_all_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1025'
    response = requests.get(url)
    data = response.json()
    pokemons = [{'name': pokemon['name'], 'id': pokemon['url'].split('/')[-2]} for pokemon in data['results']]
    for pokemon in pokemons:
        pokemon['name'] = pokemon['name'].capitalize()
    return jsonify({'pokemons': pokemons})

#POST endpoint for modify an existing POKEMON
@api_blueprint.route('/api/mod_pokemon/<pokemon_id>', methods=['POST'])
def mod_pokemon(pokemon_id):
    data = request.json
    name = data.get('name')
    pokedex_id = data.get('pokedex_id')
    level = data.get('level')
    ability_1 = data.get('ability_1')
    ability_2 = data.get('ability_2', None)
    ability_3 = data.get('ability_3', None)
    ability_4 = data.get('ability_4', None)
    owner_id = data.get('owner_id')

    if not name or not pokedex_id or not level or not ability_1 or not owner_id:
        return jsonify({'error': 'All fields are required'})

    mod_pokemon_query = f"""
                        UPDATE POKEMON SET 
                        name = :name, 
                        pokedex_id = :pokedex_id, 
                        level = :level, 
                        ability_1 = :ability_1, 
                        ability_2 = :ability_2, 
                        ability_3 = :ability_3, 
                        ability_4 = :ability_4, 
                        owner_id = :owner_id
                        WHERE id = {pokemon_id}
                        """

    try:
        with engine.connect() as connection:
            connection.execute(text(mod_pokemon_query), {
                'name': name,
                'pokedex_id': pokedex_id,
                'level': level,
                'ability_1': ability_1,
                'ability_2': ability_2,
                'ability_3': ability_3,
                'ability_4': ability_4,
                'owner_id': owner_id,
                'pokemon_id': pokemon_id
            })
        return jsonify({'message': f'Pokemon with id: {pokemon_id} modified successfully'})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})
    except Exception as e:
        return jsonify({'error': str(e)})