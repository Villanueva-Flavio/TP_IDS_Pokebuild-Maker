from flask import Blueprint
from sqlalchemy import create_engine
from sqlalchemy.engine import URL



api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api', methods=['GET'])
def api_route():
    url_object = URL.create(
        "mysql+mysqlconnector",
        username="root",
        password="1",
        host="localhost:4000",
        database="pokebuildmaker"
    )
    return str(url_object)
