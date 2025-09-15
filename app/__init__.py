from flask import Flask, render_template
from app.api.endpoints import api_bp
from app.api.enrolamiento import enrolamiento_bp
from app.api.documentos import documentos_bp
from app.api.contratos import contratos_bp
from app.api.solicitudes import solicitudes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config["SECRET_KEY"] = "supersecretkey"

    # Registrar los blueprints para los endpoints API
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(enrolamiento_bp, url_prefix='/api/enrollment')
    app.register_blueprint(documentos_bp, url_prefix='/api')
    app.register_blueprint(contratos_bp, url_prefix='/api')
    app.register_blueprint(solicitudes_bp, url_prefix='/api/requests')

    # Rutas para servir las páginas HTML
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/validar_identidad')
    def validar_identidad_page():
        return render_template('validar_identidad.html')

    @app.route('/enrolamiento')
    def enrolamiento_page():
        return render_template('enrolamiento.html')

    @app.route('/gestion_documentos')
    def gestion_documentos_page():
        return render_template('gestion_documentos.html')

    @app.route('/contratos_digitales')
    def contratos_digitales_page():
        return render_template('contratos_digitales.html')

    @app.route('/estado_solicitudes')
    def estado_solicitudes_page():
        return render_template('estado_solicitudes.html')

    return app