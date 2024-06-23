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
POKEMONS_QUERY = "SELECT * FROM POKEMON" #imp
POKEMON_ID_ROUTE = '/api/pokemon/<pokemon_id>/'
POKEMON_ID_QUERY = "SELECT * FROM POKEMON WHERE ID = "
POKEMONS_BY_USER_ROUTE = '/api/pokemons_by_user/<user_id>'
POKEMONS_BY_USER_QUERY = "SELECT * FROM POKEMON WHERE owner_id = "

BUILDS_ROUTE = '/api/builds/' #imp
BUILDS_QUERY = "SELECT * FROM BUILDS"
BUILD_ID_ROUTE = '/api/build/<build_id>/'
BUILD_ID_QUERY = "SELECT * FROM BUILDS WHERE ID = "

USERS_ROUTE = '/api/users_profiles/'
USERS_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u;"
USER_ID_ROUTE = '/api/user_profile/<user_id>/'
USER_ID_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u WHERE id = "

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

# GET endpoint for pokemon by user_id
@api_blueprint.route(POKEMONS_BY_USER_ROUTE, methods=['GET'])
def get_pokemon_by_user(user_id):
    return get_data(POKEMONS_BY_USER_QUERY + user_id)

# GET endpoint for HOME
@api_blueprint.route('/api', methods=['GET'])
def api_home():
    endpoints = {
        "pokemons": "/api/pokemons",
        "builds": "/api/builds",
        "users_profiles": "/api/users_profiles"
    }
    return jsonify(endpoints)

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

def id_must_be_an_integer(id, field_name):
    try:
        id_int = int(id)
        return id_int
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be an integer")

 #POST endpoint for adding a new USER   
@api_blueprint.route('/api/add_user', methods=['POST'])
def add_user():
    data_user = request.json  
    username = data_user.get('username')
    password = data_user.get('password')
    email = data_user.get('email')
    profile_picture = data_user.get('profile_picture')

    if not username or not password or not email:
        return jsonify({'error': 'Missing required fields (username, password, email)'})

    try:
        with engine.connect() as connection:
            add_user_query = "INSERT INTO USER (username, password, email, profile_picture) VALUES (:username, :password, :email, :profile_picture)"
            connection.execute(text(add_user_query), {
                'username': username,
                'password': password,
                'email': email,
                'profile_picture': profile_picture
            })

        return jsonify({'message': 'User added successfully'})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})

    except Exception as e:
        return jsonify({'error': str(e)})
   
#POST endpoint for modify an existing USER
@api_blueprint.route('/api/mod_user/<int:user_id>', methods=['POST'])
def mod_user(user_id):
    data_user = request.json  # Cambio: 'requests' a 'request'
    username = data_user.get('username')
    password = data_user.get('password')
    email = data_user.get('email')
    profile_picture = data_user.get('profile_picture')

    if not username or not password or not email:
        return jsonify({'error': 'Missing required fields (username, password, email)'})

    try:
        with engine.connect() as connection:
            mod_user_query = """
                UPDATE USER 
                SET username = :username, 
                    password = :password, 
                    email = :email, 
                    profile_picture = :profile_picture
                WHERE id = :user_id
            """
            connection.execute(text(mod_user_query), {
                'username': username,
                'password': password,
                'email': email,
                'profile_picture': profile_picture,
                'user_id': user_id
            })

        return jsonify({'message': f'User with ID {user_id} modified successfully'})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})

    except Exception as e:
        return jsonify({'error': str(e)})

# POST endpoint for adding a new BUILD
@api_blueprint.route(BUILDS_ROUTE, methods=['POST'])
def add_build():
    data_build = request.json
    build_name = data_build.get('build_name', '')
    owner_id = id_must_be_an_integer(data_build.get('owner_id'), 'owner_id')
    pokemon_id_1 = id_must_be_an_integer(data_build.get('pokemon_id_1'), 'pokemon_id_1')
    pokemon_id_2 = id_must_be_an_integer(data_build.get('pokemon_id_2'), 'pokemon_id_2')
    pokemon_id_3 = id_must_be_an_integer(data_build.get('pokemon_id_3'), 'pokemon_id_3')
    pokemon_id_4 = id_must_be_an_integer(data_build.get('pokemon_id_4'), 'pokemon_id_4')
    pokemon_id_5 = id_must_be_an_integer(data_build.get('pokemon_id_5'), 'pokemon_id_5')
    pokemon_id_6 = id_must_be_an_integer(data_build.get('pokemon_id_6'), 'pokemon_id_6')
    timestamp = data_build.get('timestamp', '')

    if not build_name:
        return jsonify({'Error': 'build_name must not be empty'})
    if owner_id is None:
        return jsonify({'Error': 'owner_id must not be None'})
    if pokemon_id_1 is None:
        return jsonify({'Error': 'pokemon_id_1 must not be None'})
    if timestamp is None:
        return jsonify({'Error': 'timestamp must not be None'})
    
    add_build_query = """
            INSERT INTO BUILDS 
            (build_name, owner_id, pokemon_id_1, pokemon_id_2, 
            pokemon_id_3, pokemon_id_4, pokemon_id_5, 
            pokemon_id_6, timestamp)
            VALUES 
            (:build_name, :owner_id, :pokemon_id_1, 
            :pokemon_id_2, :pokemon_id_3, :pokemon_id_4, 
            :pokemon_id_5, :pokemon_id_6, :timestamp)
        """
    
    try:
        with engine.connect() as connection:
            connection.execute(text(add_build_query), {
                'build_name': build_name,
                'owner_id': owner_id,
                'pokemon_id_1': pokemon_id_1,
                'pokemon_id_2': pokemon_id_2,
                'pokemon_id_3': pokemon_id_3,
                'pokemon_id_4': pokemon_id_4,
                'pokemon_id_5': pokemon_id_5,
                'pokemon_id_6': pokemon_id_6,
                'timestamp': timestamp
            })
        return jsonify({'Message': 'Build added successfully'})
    
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'Error': error})
    
    except Exception as e:
        return jsonify({'Error': str(e)})



#POST endpoint for delete user
@api_blueprint.route('/api/del_user/<int:user_id>', methods=['POST'])
def del_user(user_id):
    try:
        with engine.connect() as connection:
            del_user_query = "DELETE FROM USER WHERE id = :user_id"
            connection.execute(text(del_user_query), {'user_id': user_id})
        
        return jsonify({'message': f'User with ID {user_id} deleted successfully'})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})

    except Exception as e:
        return jsonify({'error': str(e)})