from flask import Flask
from app.models import db

# Función para crear la aplicación Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Registrar el blueprint con las vistas
    with app.app_context():
        from app import views
        app.register_blueprint(views.url_shortener_bp)

    return app
