from flask import Blueprint

api_bp = Blueprint('api', __name__)

from .endpoints import *  # Importar los endpoints definidos en endpoints.py

def init_app(app):
    app.register_blueprint(api_bp, url_prefix='/api')