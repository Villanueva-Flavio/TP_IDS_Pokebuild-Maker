from flask import Blueprint, render_template, request

frontend_blueprint = Blueprint('frontend', __name__)

@frontend_blueprint.route('/')
def index():
    return render_template('home.html')


@frontend_blueprint.route('/pop-up-test')
def pop_up_test():
    return render_template('pop-up-test.html')

@frontend_blueprint.route('/formulario_añadir_pokemon', methods=["POST", "GET"])
def formulario_añadir_pokemon():
    if request.method == "POST":
        name = request.form.get("pname")
        LVL = request.form.get("pLVL")
        Pokemon = request.form.get("ppokemon")
        abilidad_1 = request.form.get("pabilidad_1")
        abilidad_2 = request.form.get("pabilidad_2")
        abilidad_3 = request.form.get("pabilidad_3")
        abilidad_4 = request.form.get("pabilidad_4")
        return render_template("home.html", name=name,LVL=LVL,Pokemon=Pokemon,abilidad_1=abilidad_1,abilidad_2=abilidad_2,abilidad_3=abilidad_3,abilidad_4=abilidad_4)
    return render_template("formulario_añadir_pokemon.html")
