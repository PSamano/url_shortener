from datetime import datetime
from app import db

class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    shortcode = db.Column(db.String(10), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
