from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app import views
        app.register_blueprint(views.url_shortener_bp)

    return app
