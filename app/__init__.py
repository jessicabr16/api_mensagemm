from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def register_error_handlers(app):
    @app.errorhandler(400)
    def conteudo_vazio(error):
        return jsonify({"conteudo": "Mensagem vazia."}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"conteudo": "Mensagem não encontrada."}), 404

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.messages import messages_bp
    app.register_blueprint(messages_bp)


    register_error_handlers(app)


    return app
