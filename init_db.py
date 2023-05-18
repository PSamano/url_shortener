from app.models import db
from app import create_app

app = create_app()

# Crear las tablas de la base de datos con el contexto de la aplicación
with app.app_context():
    db.create_all()
