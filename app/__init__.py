from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Инициализация расширений
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    with app.app_context():
        try:
            # Проверка соединения с базой данных
            db.engine.connect()
            print("Успешно подключено к базе данных PostgreSQL.")
        except Exception as e:
            print("Не удалось подключиться к базе данных PostgreSQL.")
            print(e)  # Печать детали ошибки
            exit(1)  # Выход из программы, если подключение не удалось

    from app import routes, auth, models
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)


    # @app.route('/')
    # def main():
    #   return render_template('main_page.html')

    @app.route('/hello/<name>')
    def hello(name):
      return render_template('hello.html', name=name)

    @app.route('/user/<username>')
    def show_user_profile(username):
      return f'User {username}'

    @app.route('/about')
    def about():
      return '<h1>DOM</h1><a href="/">Main</a>'

    @app.route('/submit', methods=['POST'])
    def submit():
      name = request.form['name']
      return f'Hello, {name}'
    
    return app
