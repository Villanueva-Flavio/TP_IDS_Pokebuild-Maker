from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api', methods=['GET'])
def api_route():
    return 'API response'
