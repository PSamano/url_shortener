from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definir el modelo de URL
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    shortcode = db.Column(db.String(8), unique=True, nullable=False)
