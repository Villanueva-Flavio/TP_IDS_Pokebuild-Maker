from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify, Blueprint, redirect, url_for, render_template
from sqlalchemy import create_engine, text

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

@api_blueprint.route('/api/builds', methods=['GET'])
def get_builds():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM BUILDS"))
        builds = []
        for row in result:
            builds_dict = dict(row)
            builds.append(builds_dict)
    return jsonify(builds)


@api_blueprint.route('/api/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    try:
        with engine.connect() as connection:
            get_pokemon_query = text("SELECT * FROM POKEMON WHERE id = :id")
            result = connection.execute(get_pokemon_query, id=pokemon_id)
            pokemon = result.fetchone()
            pokemon_dict = dict(pokemon)
            return jsonify(pokemon_dict)
    except Exception as e:
        error_title = type(e).__name__
        error_message = "Pokemon not found"
        return redirect(url_for('error', error_title=error_title, error_message=error_message))

@api_blueprint.route('/error/<error_title>/<error_message>', methods=['GET'])
def error(error_title, error_message):
    return render_template('error_handler.html',error_title=error_title ,error_message=error_message)

@api_blueprint.route('/api', methods=['GET'])
def api_route():
    return 'Hello world from API!'


