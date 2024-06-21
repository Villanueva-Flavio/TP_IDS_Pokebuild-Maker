from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify, Blueprint, request
from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash, check_password_hash
import os, requests
from dotenv import load_dotenv
import mysql.connector

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
POST_POKEMON = '/api/add_pokemon/'
POST_POKEMON_QUERY = "INSERT INTO POKEMON (pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4, owner_id) VALUES (:pokedex_id, :level, :name, :ability_1, :ability_2, :ability_3, :ability_4, :owner_id)"
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

USER_ID_POKEMONS_ROUTE='/api/pokemons_by_user/<owner_id>'
USER_ID_POKEMONS_QUERY= "SELECT id, pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4 FROM POKEMON WHERE owner_id ="

MOVES_BY_POKEMON_ID = '/api/moves/<pokemon_id>'
GET_ALL_POKEMONS = '/api/get_all_pokemons'

DELETE_USER_POKEMON = '/api/delete_pokemon/<owner_id>/<pokemon_id>'

REGISTER_ROUTE = '/api/register/'
LOGIN_ROUTE = '/api/login/'

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

# Function to get data from the database and returns it in a json
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
    
@api_blueprint.route('POST_POKEMON', methods=['POST'])
def add_pokemon():
    try:
        pokemon_data = request.get_json()

        if pokemon_data is None:
            return jsonify({'error': 'Invalid JSON or empty request body'}), 400

        required_fields = ['pokedex_id', 'level', 'ability_1', 'owner_id']
        for field in required_fields:
            if field not in pokemon_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        pokedex_id = pokemon_data['pokedex_id']
        level = pokemon_data['level']
        name = pokemon_data.get('name', None)
        ability_1 = pokemon_data['ability_1']
        ability_2 = pokemon_data.get('ability_2', None)
        ability_3 = pokemon_data.get('ability_3', None)
        ability_4 = pokemon_data.get('ability_4', None)
        owner_id = pokemon_data['owner_id']

        with engine.connect() as connection:
            connection.execute(POST_POKEMON_QUERY, {
                'pokedex_id': pokedex_id,
                'level': level,
                'name': name,
                'ability_1': ability_1,
                'ability_2': ability_2,
                'ability_3': ability_3,
                'ability_4': ability_4,
                'owner_id': owner_id
            })

        return jsonify({'message': 'Pokemon added successfully.'}), 200

    except KeyError as e:
        return jsonify({'error': f'Missing key in JSON: {str(e)}'}), 400

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


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


# GET endpoint for getting all pokemons in the pokedex
@api_blueprint.route(GET_ALL_POKEMONS, methods=['GET'])
def get_all_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1025'
    response = requests.get(url)
    data = response.json()
    pokemons = [{'name': pokemon['name'], 'id': pokemon['url'].split('/')[-2]} for pokemon in data['results']]
    for pokemon in pokemons:
        pokemon['name'] = pokemon['name'].capitalize()
    return jsonify({'pokemons': pokemons})

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

# Function to check if the id is an integer and returns it as an integer
def to_int(id, field_name):
    try:
        id_int = int(id)
        return id_int
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be an integer")

# POST endpoint for adding a new BUILD
@api_blueprint.route(BUILDS_ROUTE, methods=['POST'])
def add_build():
    data_build = request.json
    build_name = data_build.get('build_name', '')
    owner_id = to_int(data_build.get('owner_id'), 'owner_id')
    pokemon_id_1 = to_int(data_build.get('pokemon_id_1'), 'pokemon_id_1')
    pokemon_id_2 = to_int(data_build.get('pokemon_id_2'), 'pokemon_id_2')
    pokemon_id_3 = to_int(data_build.get('pokemon_id_3'), 'pokemon_id_3')
    pokemon_id_4 = to_int(data_build.get('pokemon_id_4'), 'pokemon_id_4')
    pokemon_id_5 = to_int(data_build.get('pokemon_id_5'), 'pokemon_id_5')
    pokemon_id_6 = to_int(data_build.get('pokemon_id_6'), 'pokemon_id_6')
    timestamp = data_build.get('timestamp', '')

    if not build_name or not owner_id or not pokemon_id_1 or not timestamp:
        return jsonify({'error': 'all fields should be complete'})
    
    add_build_query = """
            INSERT INTO BUILDS 
            (build_name, owner_id, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5, pokemon_id_6, timestamp)
            VALUES 
            (:build_name, :owner_id, :pokemon_id_1, :pokemon_id_2, :pokemon_id_3, :pokemon_id_4, :pokemon_id_5, :pokemon_id_6, :timestamp)
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
        return jsonify({'message': 'Build added successfully'})
    
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})
    
    except Exception as e:
        return jsonify({'error': str(e)})

@api_blueprint.route(REGISTER_ROUTE, methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    profile_picture = data.get('profile_picture')

    if not username or not password or not email or not profile_picture:
        return jsonify({'error': 'Username, password, email and profile_picture are required'})
    
    add_user_query = """
        INSERT INTO USER (username, password, email, profile_picture)
        VALUES (:username, :password, :email, :profile_picture)
    """
    
    try:
        with engine.connect() as connection:
            connection.execute(add_user_query), {
                'username': username,
                'password': password,
                'email': email,
                'profile_picture': profile_picture
            }
        return jsonify({"message": "User registered successfully"})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})
    except Exception as e:
        return jsonify({'error': str(e)})

@api_blueprint.route(LOGIN_ROUTE, methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'})

    try:
        check_login_query = "SELECT id, username, password FROM USER WHERE email = :email"
        with engine.connect() as connection:
            result = connection.execute(text(check_login_query), {'email': email})
            user = result.fetchone()
        
        if user:
            user_id, username, hashed_password = user
            if check_password_hash(hashed_password, password):
                return jsonify({"message": "Login successful", "user_id": user_id, "username": username})
            else:
                return jsonify({"error": "Invalid password"})
        else:
            return jsonify({"error": "Email not found"})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route(USER_ID_POKEMONS_ROUTE, methods=['GET'])
def get_pokemons_by_user(owner_id):
    return get_data(USER_ID_POKEMONS_QUERY + owner_id)

def reorder_nulls_to_end():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = conn.cursor()

        query = "SELECT * FROM BUILDS"
        cursor.execute(query)
        builds = cursor.fetchall()

        updated_builds = []

        for build in builds:
            pokemon_ids = [build[2], build[3], build[4], build[5], build[6], build[7]]
            
            sorted_pokemon_ids = sorted(pokemon_ids, key=lambda x: x is None)
            
            updated_build = (
                build[1],  
                sorted_pokemon_ids[0],
                sorted_pokemon_ids[1],
                sorted_pokemon_ids[2],
                sorted_pokemon_ids[3],
                sorted_pokemon_ids[4],
                sorted_pokemon_ids[5],
                build[8],
                build[9]
            )
            
            updated_builds.append(updated_build)

        update_query = "UPDATE BUILDS SET pokemon_id_1 = %s, pokemon_id_2 = %s, pokemon_id_3 = %s, pokemon_id_4 = %s, pokemon_id_5 = %s, pokemon_id_6 = %s WHERE id = %s"
        for idx, updated_build in enumerate(updated_builds):
            cursor.execute(update_query, (updated_build[1], updated_build[2], updated_build[3], updated_build[4], updated_build[5], updated_build[6], builds[idx][0]))

        conn.commit()

        cursor.close()
        conn.close()

        print("Tabla BUILDS actualizada exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


@api_blueprint.route(DELETE_USER_POKEMON, methods=['POST'])
def delete_pokemon(pokemon_id, owner_id):
    try:
        with engine.connect() as connection:
            with connection.begin():
                # Verificar si el Pokémon pertenece al usuario
                verify_query = text("SELECT * FROM POKEMON WHERE id = :id AND owner_id = :owner_id")
                result = connection.execute(verify_query, {"id": pokemon_id, "owner_id": owner_id}).fetchone()
                
                if not result:
                    return {"error": f"Pokemon con id {pokemon_id} no pertenece al usuario con id {owner_id}."}, 404

                # Eliminar el Pokémon
                delete_pokemon_query = text("DELETE FROM POKEMON WHERE id = :id")
                connection.execute(delete_pokemon_query, {"id": pokemon_id})

                # Eliminar filas de la tabla BUILDS
                delete_builds_query = text("DELETE FROM BUILDS WHERE pokemon_id_1 = :pokemon_id OR pokemon_id_2 = :pokemon_id OR pokemon_id_3 = :pokemon_id OR pokemon_id_4 = :pokemon_id OR pokemon_id_5 = :pokemon_id OR pokemon_id_6 = :pokemon_id")
                connection.execute(delete_builds_query, {"pokemon_id": pokemon_id})

            #reorder_nulls_to_end()

        return {"message": f"Pokémon con id {pokemon_id} eliminado exitosamente."}, 200

    except SQLAlchemyError as e:
        error_message = f"Error al conectarse a la base de datos: {e}"
        print(error_message)
        return {"error": error_message}, 500
