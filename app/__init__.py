from flask import Flask
import os
from app.config import config

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app