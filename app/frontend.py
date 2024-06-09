from flask import Blueprint, render_template

frontend_blueprint = Blueprint('frontend', __name__)

@frontend_blueprint.route('/')
def index():
    return render_template('home.html')


@frontend_blueprint.route('/pop-up-test')
def pop_up_test():
    return render_template('pop-up-test.html')

@frontend_blueprint.route('/login_register')
def login_register():
    return render_template('login_register.html')