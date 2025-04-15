from flask import Flask
import os
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app