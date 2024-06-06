from flask import jsonify, Blueprint
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
api_blueprint = Blueprint('api', __name__)

# uso el puerto 3306 para MySQL ya que es el puerto interno de MySQL en el contenedor
engine = create_engine('mysql+mysqlconnector://root:1@pokebuild-db:3306/pokebuildmaker')

@api_blueprint.route('/build/<id>', methods = ['GET'])
def get_user(id):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM BUILDS WHERE id = {id}"))
        build = []
        for row in result:
            build_dict = dict(row)
            build.append(build_dict)
    return jsonify(build)


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
