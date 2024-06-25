from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify, Blueprint, request
from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash, check_password_hash
import os, requests
from dotenv import load_dotenv
import re
import mysql.connector


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
POST_POKEMON = '/api/add_pokemon/'
POST_POKEMON_QUERY = """
INSERT INTO POKEMON (pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4, owner_id)
VALUES (:pokedex_id, :level, :name, :ability_1, :ability_2, :ability_3, :ability_4, :owner_id)
"""
DELETE_USER_POKEMON = '/api/delete_pokemon/<int:owner_id>/<int:pokemon_id>'
POKEMONS_MOVES_ROUTE='/api/moves/<pokemon_id>'
POKEMONS_GET_ALL_ROUTE='/api/get_all_pokemons'
POKEMONS_TYPES_ROUTE='/api/types/<pokemon_id>/'

DELETE_USER_POKEMON = '/api/delete_pokemon/<int:owner_id>/<int:pokemon_id>'

BUILDS_ROUTE = '/api/builds/'
BUILDS_QUERY = "SELECT * FROM BUILDS"
BUILD_ID_ROUTE = '/api/build/<build_id>/'
BUILD_ID_QUERY = "SELECT * FROM BUILDS WHERE ID = "
ADD_BUILD_ROUTE='/api/add_build/'

USER_ID_POKEMONS_ROUTE='/api/pokemons_by_user/<owner_id>'
USER_ID_POKEMONS_QUERY= "SELECT id, pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4 FROM POKEMON WHERE owner_id ="
USER_ID_BUILDS_ROUTE='/api/builds_by_user/<owner_id>'
USER_ID_BUILDS_QUERY = "SELECT id, build_name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5, pokemon_id_6, timestamp FROM BUILDS WHERE owner_id ="


USERS_ROUTE = '/api/users_profiles/'
USERS_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u;"
USER_ID_ROUTE = '/api/user_profile/<user_id>/'
USER_ID_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u WHERE id = "
REGISTER = '/api/register/'
LOGIN = '/api/login/'

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
@api_blueprint.route(POST_POKEMON, methods=['POST'])
def add_pokemon():
    try:
        pokemon_data = request.get_json()

        if pokemon_data is None:
            return jsonify({'error': 'Invalid JSON or empty request body'}), 400

        required_fields = ['pokedex_id', 'level', 'ability_1', 'owner_id']
        for field in required_fields:
            if field not in pokemon_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
            
        abilities = [
            pokemon_data.get('ability_1'),
            pokemon_data.get('ability_2'),
            pokemon_data.get('ability_3'),
            pokemon_data.get('ability_4')
        ]
        if all(ability in (None, '') for ability in abilities):
            return jsonify({'error': 'At least one ability is required'}), 400
        with engine.connect() as connection:
            connection.execute(text(POST_POKEMON_QUERY), {
                'pokedex_id': pokemon_data['pokedex_id'],
                'level': pokemon_data['level'],
                'name': pokemon_data.get('name', None),
                'ability_1': pokemon_data['ability_1'],
                'ability_2': pokemon_data.get('ability_2', None),
                'ability_3': pokemon_data.get('ability_3', None),
                'ability_4': pokemon_data.get('ability_4', None),
                'owner_id': pokemon_data['owner_id']
            })

        return jsonify({'message': 'Pokemon added successfully.'}), 200

    except KeyError as e:
        return jsonify({'error': f'Missing key in JSON: {str(e)}'}), 400

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@api_blueprint.route(POKEMONS_MOVES_ROUTE, methods=['GET'])
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

@api_blueprint.route(POKEMONS_GET_ALL_ROUTE, methods=['GET'])
def get_all_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1025'
    response = requests.get(url)
    data = response.json()
    pokemons = [{'name': pokemon['name'], 'id': pokemon['url'].split('/')[-2]} for pokemon in data['results']]
    for pokemon in pokemons:
        pokemon['name'] = pokemon['name'].capitalize()
    return jsonify({'pokemons': pokemons})


@api_blueprint.route(POKEMONS_TYPES_ROUTE, methods=['GET'])
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


    if not name or not pokedex_id or not level or not owner_id:
        return jsonify({'error': 'All fields are required'})
    abilities = [
        data.get('ability_1'),
        data.get('ability_2'),
        data.get('ability_3'),
        data.get('ability_4')
    ]
    if all(ability in (None, '') for ability in abilities):
        return jsonify({'error': 'At least one ability is required'}), 400
      
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
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def is_valid_password(password):
    # Minimum 8 characters, at least one letter and one number
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(regex, password) is not None


#DELETE endport for POKEMON by ID
@api_blueprint.route(DELETE_USER_POKEMON, methods=['POST'])
def delete_pokemon(pokemon_id, owner_id):
    try:
        with engine.connect() as connection:
            with connection.begin():

                delete_pokemon_query = text("DELETE FROM POKEMON WHERE id = :id AND owner_id = :owner_id")
                connection.execute(delete_pokemon_query, {"id": pokemon_id, "owner_id":owner_id})

                update_cases = ', '.join([
                    f"pokemon_id_{i} = CASE WHEN pokemon_id_{i} = :pokemon_id THEN NULL ELSE pokemon_id_{i} END"
                    for i in range(1, 7)
                ])

                update_builds_query = text(f"""
                UPDATE BUILDS
                SET {update_cases}
                """)
                connection.execute(update_builds_query, {"pokemon_id": pokemon_id})

        reorder_nulls_to_end()

        return {"message": f"Pokémon con id {pokemon_id} eliminado exitosamente."}, 200

    except SQLAlchemyError as e:
        error_message = f"Error al conectarse a la base de datos: {e}"
        print(error_message)
        return {"error": error_message}, 500    

# POST endpoint for adding a new BUILD
@api_blueprint.route(ADD_BUILD_ROUTE, methods=['POST'])
def add_build():
    data_build = request.json

    build_name = data_build.get('build_name', '')
    owner_id = data_build.get('owner_id', None)
    pokemon_id_1 = data_build.get('pokemon_id_1', None)
    pokemon_id_2 = data_build.get('pokemon_id_2', None)
    pokemon_id_3 = data_build.get('pokemon_id_3', None)
    pokemon_id_4 = data_build.get('pokemon_id_4', None)
    pokemon_id_5 = data_build.get('pokemon_id_5', None)
    pokemon_id_6 = data_build.get('pokemon_id_6', None)
    timestamp = data_build.get('timestamp', '')

    # Validar los valores recibidos
    if not build_name:
        return jsonify({'Error': 'build_name must not be empty'})
    if owner_id is None:
        return jsonify({'Error': 'owner_id must not be None'})
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
    

@api_blueprint.route(REGISTER, methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    profile_picture = data.get('profile_picture')

    # Check for missing fields
    if not username or not password or not email:
        return jsonify({'error': 'Username, password and email are required'}), 400
    
    # Validate email
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email'}), 400

    # Validate password
    if not is_valid_password(password):
        return jsonify({'error': 'Invalid password'}), 400
    
    # Creo la consulta SQL para verificar si username o email ya existe
    check_user_query = """
        SELECT * FROM USER WHERE username = %s OR email = %s
    """

    try:
        with engine.connect() as connection:
            result = connection.execute(check_user_query, (username, email)).fetchone()
            if result:
                if result['username'] == username:
                    return jsonify({'error': 'That username is already taken'}), 400
                if result['email'] == email:
                    return jsonify({'error': 'That email is already registered'}), 400

            # Hash the password
            hashed_password = generate_password_hash(password)
            
            add_user_query = """
                INSERT INTO USER (username, password, email, profile_picture)
                VALUES (%s, %s, %s, %s)
            """
            connection.execute(add_user_query, (username, hashed_password, email, profile_picture))
        return jsonify({"message": "User registered successfully"}), 201

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route(LOGIN, methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    get_user_query = """
        SELECT email, password FROM USER WHERE email = %s
    """

    try:
        with engine.connect() as connection:
            result = connection.execute(get_user_query, (email,))
            user = result.fetchone()

            if user is None:
                return jsonify({'error': 'Invalid email or password'}), 401

            stored_password = user['password']

            if check_password_hash(stored_password, password):
                return jsonify({'message': 'Login successful'}), 200
            else:
                return jsonify({'error': 'Invalid email or password'}), 401

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@api_blueprint.route(USER_ID_BUILDS_ROUTE, methods=['GET'])
def get_build_by_user(owner_id):
    return get_data( USER_ID_BUILDS_QUERY + owner_id)


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