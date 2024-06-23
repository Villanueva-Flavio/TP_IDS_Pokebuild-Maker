from flask import Flask
from api import api_blueprint  # Importa desde api.py
from frontend import frontend_blueprint  # Importa desde frontend.py

app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(frontend_blueprint)

@api_blueprint.route('/api/add_pokemon', methods=['POST'])
def add_pokemon():
    data = request.json
    name = data.get('name')
    pokedex_id = data.get('pokedex_id')
    level = data.get('level')
    ability_1 = data.get('ability_1')
    ability_2 = data.get('ability_2')
    ability_3 = data.get('ability_3')
    ability_4 = data.get('ability_4')
    owner_id = data.get('owner_id')

    if not name or not pokedex_id or not level or not ability_1 or not ability_2 or not ability_3 or not ability_4 or not owner_id:
        return jsonify({'error': 'All fields are required'})
    
    add_pokemon_query = """
        INSERT INTO POKEMON (name, pokedex_id, level, ability_1, ability_2, ability_3, ability_4, owner_id)
        VALUES (:name, :pokedex_id, :level, :ability_1, :ability_2, :ability_3, :ability_4, :owner_id)
    """

    try:
        with engine.connect() as connection:
            connection.execute(text(add_pokemon_query), {
                'name': name,
                'pokedex_id': pokedex_id,
                'level': level,
                'ability_1': ability_1,
                'ability_2': ability_2,
                'ability_3': ability_3,
                'ability_4': ability_4,
                'owner_id': owner_id
            })
        return jsonify({'message': 'Pokemon added successfully'})
    
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error})
    except Exception as e:
        return jsonify({'error': str(e)})

