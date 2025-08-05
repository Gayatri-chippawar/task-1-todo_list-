from flask import Flask
from .config import Config
from .db import db
from flask_cors import CORS
from .routes.tasks import tasks_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

    db.init_app(app)

    from .routes.tasks import tasks_bp
    from .routes.comments import comments_bp
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks/')
    app.register_blueprint(comments_bp, url_prefix='/api/comments/')

    return app
