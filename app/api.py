from flask import jsonify, Blueprint
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
api_blueprint = Blueprint('api', __name__)

# uso el puerto 3306 para MySQL ya que es el puerto interno de MySQL en el contenedor
engine = create_engine('mysql+mysqlconnector://root:1@pokebuild-db:3306/pokebuildmaker')

@api_blueprint.route('/build/<id>', methods = ['GET'])
def get_user(id):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM BUILDS WHERE id = {id}"))
    if result.rowcount !=0:
        data = {}
        row = result.first()
        data['id'] = row['id']
        data['build_name'] = row['build_name']
        data['pokemon_id_1'] = row['pokemon_id_1']
        data['pokemon_id_2'] = row['pokemon_id_2']
        data['pokemon_id_3'] = row['pokemon_id_3']
        data['pokemon_id_4'] = row['pokemon_id_4']
        data['pokemon_id_5'] = row['pokemon_id_5']
        data['pokemon_id_6'] = row['pokemon_id_6']
        data['timestamp'] = row['timestamp']
        data['owner_id'] = row['owner_id']
        return jsonify(data), 200
    else:
        return jsonify({"message": "El usuario no existe"}), 404


@api_blueprint.route('/api/pokemons', methods=['GET'])
def get_pokemons():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM POKEMON"))
        pokemons = []
        for row in result:
            pokemon_dict = dict(row)
            pokemons.append(pokemon_dict)
    return jsonify(pokemons)

# Otros endpoints de tu API
@api_blueprint.route('/api', methods=['GET'])
def api_route():
    return 'Hello world from API!'
