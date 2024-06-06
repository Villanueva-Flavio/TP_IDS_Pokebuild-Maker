from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify, Blueprint, redirect, url_for, render_template
from sqlalchemy import create_engine, text

api_blueprint = Blueprint('api', __name__)

# uso el puerto 3306 para MySQL ya que es el puerto interno de MySQL en el contenedor
engine = create_engine('mysql+mysqlconnector://root:1@pokebuild-db:3306/pokebuildmaker')

@api_blueprint.route('/api/users', methods=['GET'])
def get_users_profiles():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT username, email, profile_picture FROM USER"))
        users = []
        for row in result:
            user_dict = dict(row)
            users.append(user_dict)
    return jsonify(users)

@api_blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_profile_by_id(user_id):
    try:
        with engine.connect() as connection:
            get_user_query = text("SELECT username, email, profile_picture FROM USER WHERE id = :id")
            result = connection.execute(get_user_query, id=user_id)
            user = result.fetchone()
            user_dict = dict(user)
            return jsonify(user_dict)
    
    except Exception as e:
        error_title = type(e).__name__
        error_message = "User not found"
        return redirect(url_for('error', error_title=error_title, error_message=error_message))

@api_blueprint.route('/error/<error_title>/<error_message>', methods=['GET'])
def error(error_title, error_message):
    return render_template('error_handler.html',error_title=error_title ,error_message=error_message)

@api_blueprint.route('/api', methods=['GET'])
def api_route():
    return 'Hello world from API!'