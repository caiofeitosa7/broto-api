from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rotas e blueprints
    from app.views import main
    app.register_blueprint(main)

    return app
