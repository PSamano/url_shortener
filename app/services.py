from app import db
from app.models import URL, db

def add_short_url(original_url, shortcode):
    # Verifica si la URL original ya existe en la base de datos
    existing_short_url = URL.query.filter_by(original_url=original_url).first()

    # Si la URL ya existe, devuelve el shortcode existente
    if existing_short_url:
        return existing_short_url

    # Si la URL no existe, crea un nuevo shortcode y lo guarda en la base de datos
    short_url = URL(original_url=original_url, shortcode=shortcode)
    db.session.add(short_url)
    db.session.commit()
    return short_url

def get_original_url(shortcode):
    # Busca la url original en la base de datos y la retorna
    return URL.query.filter_by(shortcode=shortcode).first()
