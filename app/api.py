from flask import jsonify, Blueprint, request, session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import mysql.connector, traceback, re
from constants import *

api_blueprint = Blueprint('api', __name__)
api_blueprint.permanent_session_lifetime = timedelta(minutes=1)

db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)


def reorder_nulls_to_end():
    try:
        conn = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute(BUILDS_QUERY)
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

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_data(query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            data = []
            columns = result.keys()
            for row in result:
                data_dict = dict(zip(columns, row))
                data.append(data_dict)

        return jsonify(data[0]) if len(data) == 1 else jsonify(data)

    except SQLAlchemyError as e:
        return jsonify({'error': str(e.__dict__['orig'])})
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def is_valid_password(password):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(regex, password) is not None

# GET endpoint for HOME
@api_blueprint.route('/api', methods=['GET'], strict_slashes=False)
def api_home():
    endpoints = {
        "pokemons": "/api/pokemons",
        "builds": "/api/builds",
        "users_profiles": "/api/users_profiles"
    }
    return jsonify(endpoints)

# GET endpoint for POKEMONS
@api_blueprint.route(POKEMONS_ROUTE, methods=['GET'], strict_slashes=False)
def get_pokemons():
    return get_data(POKEMONS_QUERY)

# GET endpoint for POKEMON by ID
@api_blueprint.route(POKEMON_ID_ROUTE, methods=['GET'], strict_slashes=False)
def get_pokemon_by_id(pokemon_id):
    return get_data(POKEMON_ID_QUERY + pokemon_id)

# GET endpoint for BUILDS
@api_blueprint.route(BUILDS_ROUTE, methods=['GET'], strict_slashes=False)
def get_builds():
    return get_data(BUILDS_QUERY)

# GET endpoint for BUILD by ID
@api_blueprint.route(BUILD_ID_ROUTE, methods=['GET'], strict_slashes=False)
def get_build_by_id(build_id):
    return get_data(BUILD_ID_QUERY + build_id)

# GET endpoint for USERS
@api_blueprint.route(USERS_ROUTE, methods=['GET'], strict_slashes=False)
def get_users_profiles():
    return get_data(USERS_QUERY)

# GET endpoint for USER by ID
@api_blueprint.route(USER_ID_ROUTE, methods=['GET'], strict_slashes=False)
def get_user_profile(user_id):
    return get_data(USER_ID_QUERY + user_id)

# GET endpoints for Pokemons by owner_id
@api_blueprint.route(USER_ID_POKEMONS_ROUTE, methods=['GET'], strict_slashes=False)
def get_pokemons_by_user(owner_id):
    return get_data(USER_ID_POKEMONS_QUERY + owner_id)

@api_blueprint.route(POKEMONS_MOVES_ROUTE, methods=['GET'], strict_slashes=False)
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

@api_blueprint.route(POKEMONS_GET_ALL_ROUTE, methods=['GET'], strict_slashes=False)
def get_all_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1025'
    response = requests.get(url)
    data = response.json()
    pokemons = [{'name': pokemon['name'], 'id': pokemon['url'].split('/')[-2]} for pokemon in data['results']]
    for pokemon in pokemons:
        pokemon['name'] = pokemon['name'].capitalize()
    return jsonify({'pokemons': pokemons})

@api_blueprint.route(POKEMONS_TYPES_ROUTE, methods=['GET'], strict_slashes=False)
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

        return jsonify({'pokemon_type': list(pokemon_type), 'good_against': list(good_against), 'bad_against': list(bad_against)})
    
    else:
        return jsonify({'error': 'Pokemon not found'}), 400

@api_blueprint.route(POST_POKEMON, methods=['POST'], strict_slashes=False)
def add_pokemon():
    try:
        pokemon_data = request.get_json()
        if pokemon_data is None:
            return jsonify({'error': 'Invalid JSON or empty request body'}), 400

        required_fields = ['pokedex_id', 'level', 'ability_1', 'owner_id']
        for field in required_fields:
            if field not in pokemon_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        abilities = [pokemon_data.get('ability_1'), pokemon_data.get('ability_2'), pokemon_data.get('ability_3'), pokemon_data.get('ability_4')]
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

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500

#POST endpoint for modify an existing POKEMON
@api_blueprint.route(MODIFY_POKEMON_ROUTE, methods=['POST'], strict_slashes=False)
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
    
    abilities = [data.get('ability_1'), data.get('ability_2'), data.get('ability_3'), data.get('ability_4')]
    if all(ability in (None, '') for ability in abilities):
        return jsonify({'error': 'At least one ability is required'}), 400
    
    try:
        with engine.connect() as connection:
            connection.execute((MOD_POKEMON_QUERY), {
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

#DELETE endpoint for POKEMON by ID
@api_blueprint.route(DELETE_USER_POKEMON, methods=['POST'], strict_slashes=False)
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

                update_builds_query = text(f"""UPDATE BUILDS SET {update_cases}""")
                connection.execute(update_builds_query, {"pokemon_id": pokemon_id})

        reorder_nulls_to_end()

        return {"message": f"Pokémon con id {pokemon_id} eliminado exitosamente."}, 200

    except SQLAlchemyError as e:
        error_message = f"Error al conectarse a la base de datos: {e}"
        print(error_message)
        return {"error": error_message}, 500    

# POST endpoint for adding a new BUILD
@api_blueprint.route(ADD_BUILD_ROUTE, methods=['POST'], strict_slashes=False)
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
    
    if not build_name or owner_id is None or timestamp is None:
        return jsonify({'Error': 'A field is missing'})
    
    try:
        with engine.connect() as connection:
            connection.execute(text(ADD_BUILD_QUERY), {
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

# POST endpoint for modify an existing BUILD
@api_blueprint.route(MOD_BUILD_ROUTE, methods=['POST'], strict_slashes=False)
def mod_build(build_id):
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

    if not build_name or owner_id is None or timestamp is None:
        return jsonify({'Error': 'A field is missing'})

    try:
        with engine.connect() as connection:
            connection.execute(text(MOD_BUILD_QUERY), {
                'build_name': build_name,
                'owner_id': owner_id,
                'pokemon_id_1': pokemon_id_1,
                'pokemon_id_2': pokemon_id_2,
                'pokemon_id_3': pokemon_id_3,
                'pokemon_id_4': pokemon_id_4,
                'pokemon_id_5': pokemon_id_5,
                'pokemon_id_6': pokemon_id_6,
                'timestamp': timestamp,
                'build_id': build_id
            })
        return jsonify({'Message': f'Build with id: {build_id} modified successfully'})

    except SQLAlchemyError as e:
        return jsonify({'Error1': str(e.__dict__['orig'])})

@api_blueprint.route(REGISTER, methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    profile_picture = data.get('profile_picture')

    if not username or not password or not email:
        return jsonify({'error': 'Username, password and email are required'}), 400
    
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email'}), 400

    if not is_valid_password(password):
        return jsonify({'error': 'Invalid password'}), 400
    
    try:
        with engine.connect() as connection:
            result = connection.execute(text(CHECK_USER_QUERY), {
                'username': username,
                'email': email
            }).fetchone()
            if result and (result['username'] == username or result['email'] == email):
                return jsonify({'error': 'That username or email is already taken'}), 400
            
            hashed_password = generate_password_hash(password)
            connection.execute(text(ADD_USER_QUERY), {
                'username': username,
                'password': hashed_password,
                'email': email,
                'profile_picture': profile_picture
            })
            connection.commit()
        
        return jsonify({"message": "User registered successfully"}), 201

    except SQLAlchemyError as e:
        error_message = f"SQLAlchemy error: {str(e)}"
        traceback.print_exc()  # Esto imprimirá el traceback en la consola del servidor
        return jsonify({'error': error_message}), 500
    except Exception as e:
        error_message = f"Error: {str(e)}"
        traceback.print_exc()  # Esto imprimirá el traceback en la consola del servidor
        return jsonify({'error': error_message}), 500

@api_blueprint.route(LOGIN, methods=['POST'], strict_slashes=False)
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        with engine.connect() as connection:
            query = text(GET_USER_QUERY)
            result = connection.execute(query, {'email': email})
            user = result.fetchone()
            if user is None or not check_password_hash(user[2], password):
                return jsonify({'error': 'Invalid email or password'}), 401
            
            session['user_id'] = user[0]
            return jsonify({'message': 'Login successful'}), 200

    except SQLAlchemyError as e:
        error = str(e)
        return jsonify({'error': error}), 500

@api_blueprint.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200
    
@api_blueprint.route(USER_ID_BUILDS_ROUTE, methods=['GET'], strict_slashes=False)
def get_build_by_user(owner_id):
    return get_data( USER_ID_BUILDS_QUERY + owner_id)


@api_blueprint.route('/api/mod_user/<int:user_id>', methods=['POST'], strict_slashes=False)
def mod_user(user_id):
    try:
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))
        email = request.form.get('email')
        profile_picture = request.files.get('profile_picture')

        if not username or not password or not email:
            return jsonify({'error': 'Missing required fields (username, password, email)'})

        with engine.connect() as connection:
            connection.execute(text(MOD_USER_QUERY), {'username': username, 'password': password, 'email': email, 'profile_picture': profile_picture.read() if profile_picture else None, 'user_id': user_id})
        return jsonify({'message': f'User with ID {user_id} modified successfully'})

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})

#POST endpoint for delete user
@api_blueprint.route(DEL_USER_ROUTE, methods=['POST'], strict_slashes=False)
def del_user(user_id):
    try:
        with engine.connect() as connection:
            connection.execute(DEL_USER_QUERY + user_id)
        return jsonify({'message': f'User with ID {user_id} deleted successfully'})
        
    except SQLAlchemyError as e:
        return jsonify({'error': str(e.__dict__['orig'])})

# POST endpoint para eliminar una BUILD por su ID (primary key de la BUILD)
@api_blueprint.route(DELETE_BUILD_ROUTE, methods=['POST'], strict_slashes=False)
def delete_build():
    data = request.json
    build_id = data.get('build_id')
    if not build_id:
        return jsonify({'error': 'build_id is required'})

    try:
        with engine.connect() as connection:            
            result = connection.execute(DELETE_BUILD_QUERY + build_id)
            if result.rowcount == 0:
                return jsonify({'error': f'Build with id {build_id} not found'})
            return jsonify({'message': f'Build with id {build_id} deleted successfully'})

    except SQLAlchemyError as e:
        return jsonify({'error': str(e.__dict__['orig'])})