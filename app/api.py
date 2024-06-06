from flask import jsonify, Blueprint
from sqlalchemy import create_engine, text

api_blueprint = Blueprint('api', __name__)

engine = create_engine('mysql+mysqlconnector://root:1@pokebuild-db:3306/pokebuildmaker')

@api_blueprint.route('/api/builds', methods=['GET'])
def get_builds():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM BUILDS"))
        builds = []
        for row in result:
            builds_dict = dict(row)
            builds.append(builds_dict)
    return jsonify(builds)

@api_blueprint.route('/api', methods=['GET'])
def api_route():
    return 'Hello world from API!'


