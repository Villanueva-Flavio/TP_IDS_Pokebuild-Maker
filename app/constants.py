import os
from dotenv import load_dotenv

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

load_dotenv()

POKEMONS_ROUTE = '/api/pokemons/'
POKEMON_ID_ROUTE = '/api/pokemon/<pokemon_id>/'
POKEMONS_MOVES_ROUTE='/api/moves/<pokemon_id>'
POKEMONS_GET_ALL_ROUTE='/api/get_all_pokemons'
POKEMONS_TYPES_ROUTE='/api/types/<pokemon_id>/'
BUILD_ID_ROUTE = '/api/build/<build_id>/'
BUILDS_ROUTE = '/api/builds/'
USER_ID_POKEMONS_ROUTE='/api/pokemons_by_user/<owner_id>'
USER_ID_BUILDS_ROUTE='/api/builds_by_user/<owner_id>'
USERS_ROUTE = '/api/users_profiles/'
USER_ID_ROUTE = '/api/user_profile/<user_id>/'
USER_ID_POKEMONS_ROUTE='/api/pokemons_by_user/<owner_id>'
ADD_BUILD_ROUTE='/api/add_build/'
POST_POKEMON = '/api/add_pokemon/'
REGISTER = '/api/register/'
LOGIN = '/api/login/'
DELETE_USER_POKEMON = '/api/delete_pokemon/<int:owner_id>/<int:pokemon_id>'
MODIFY_POKEMON_ROUTE = '/api/mod_pokemon/<pokemon_id>'
MOD_BUILD_ROUTE = '/api/mod_build/<build_id>'
MOD_USER_ROUTE = '/api/mod_user/<user_id>'
DEL_USER_ROUTE = '/api/del_user/<user_id>'
DELETE_BUILD_ROUTE = '/api/delete_build/'

ADD_USER_QUERY = """INSERT INTO USER (username, password, email, profile_picture) VALUES (:username, :password, :email, :profile_picture)"""
ADD_BUILD_QUERY = """INSERT INTO BUILDS (build_name, owner_id, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5, pokemon_id_6, timestamp) VALUES (:build_name, :owner_id, :pokemon_id_1, :pokemon_id_2, :pokemon_id_3, :pokemon_id_4, :pokemon_id_5, :pokemon_id_6, :timestamp)"""
POST_POKEMON_QUERY = """INSERT INTO POKEMON (pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4, owner_id) VALUES (:pokedex_id, :level, :name, :ability_1, :ability_2, :ability_3, :ability_4, :owner_id)"""

MOD_BUILD_QUERY = """UPDATE BUILDS SET build_name = :build_name, owner_id = :owner_id, pokemon_id_1 = :pokemon_id_1, pokemon_id_2 = :pokemon_id_2, pokemon_id_3 = :pokemon_id_3, pokemon_id_4 = :pokemon_id_4, pokemon_id_5 = :pokemon_id_5, pokemon_id_6 = :pokemon_id_6, timestamp = :timestamp WHERE id = :build_id"""
MOD_USER_QUERY = """UPDATE USER SET username = :username, password = :password, email = :email, profile_picture = :profile_picture WHERE id = :user_id"""
MOD_POKEMON_QUERY = """UPDATE POKEMON SET name = :name, pokedex_id = :pokedex_id, level = :level, ability_1 = :ability_1, ability_2 = :ability_2, ability_3 = :ability_3, ability_4 = :ability_4, owner_id = :owner_id WHERE id = :pokemon_id"""
UPDATE_QUERY = "UPDATE BUILDS SET pokemon_id_1 = %s, pokemon_id_2 = %s, pokemon_id_3 = %s, pokemon_id_4 = %s, pokemon_id_5 = %s, pokemon_id_6 = %s WHERE id = %s"

POKEMONS_QUERY = "SELECT * FROM POKEMON"
POKEMON_ID_QUERY = "SELECT * FROM POKEMON WHERE ID = "
USER_ID_POKEMONS_QUERY= "SELECT id, pokedex_id, level, name, ability_1, ability_2, ability_3, ability_4 FROM POKEMON WHERE owner_id ="
BUILDS_QUERY = "SELECT * FROM BUILDS"
BUILD_ID_QUERY = "SELECT * FROM BUILDS WHERE ID = "
USER_ID_BUILDS_QUERY = "SELECT id, build_name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5, pokemon_id_6, timestamp FROM BUILDS WHERE owner_id ="
CHECK_USER_QUERY = "SELECT * FROM USER WHERE username = :username OR email = :email"
GET_USER_QUERY = """SELECT * FROM USER WHERE email = :email"""
USERS_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u;"
USER_ID_QUERY = "SELECT u.id, u.username, u.profile_picture, (SELECT COUNT(*) FROM POKEMON p WHERE p.owner_id = u.id) AS pokemon_count, (SELECT COUNT(*) FROM BUILDS b WHERE b.owner_id = u.id) AS build_count FROM USER u WHERE id = "

DELETE_POKEMON_QUERY = "DELETE FROM POKEMON WHERE id = :id AND owner_id = :owner_id"
DELETE_BUILD_QUERY = "DELETE FROM BUILDS WHERE id = '"
DEL_USER_QUERY = "DELETE FROM USER WHERE id = "