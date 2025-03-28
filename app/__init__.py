import os
from flask import Flask, send_from_directory
from flask_cors import CORS

from app.config.settings import Config
from app.routes.api import api_bp

def create_app(config_class=Config):
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, static_url_path='')
    app.config.from_object(config_class)
    
    CORS(app)
    
    app.register_blueprint(api_bp)
    
    @app.route('/static/<path:filename>')
    def serve_static(filename):
        static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')
        return send_from_directory(static_dir, filename)
    
    return app