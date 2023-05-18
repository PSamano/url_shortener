from app import db
from app.models import URL, db

def add_short_url(original_url, shortcode):
    short_url = URL(original_url=original_url, shortcode=shortcode)
    db.session.add(short_url)
    db.session.commit()
    return short_url

def get_original_url(shortcode):
    return URL.query.filter_by(shortcode=shortcode).first()
