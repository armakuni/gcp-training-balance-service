from flask import Flask

from balance_service.app.controllers.swagger import setup_swagger
from balance_service.app.controllers.health import health
from balance_service.app.controllers.balance import balance


def create(config, balance_repository):
    app = Flask(__name__)
    app.config.from_object(config)
    app.balance_repository = balance_repository
    register_blueprints(app)

    app.register_blueprint(setup_swagger(), url_prefix=config.SWAGGER_URL)
    return app


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(health)
    app.register_blueprint(balance)
