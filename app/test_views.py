import json
import pytest
from app.services import add_short_url
from app import create_app, db
from app.models import URL
from app.utils import generate_shortcode

app = create_app()

@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as test_client:
        with app.app_context():
            db.create_all()
        yield test_client
        with app.app_context():
            db.drop_all()

def test_shorten_url(test_client):
    original_url = "https://www.example.com"
    response = test_client.post('/shorten', data=json.dumps({"url": original_url}), content_type='application/json')
    
    assert response.status_code == 200
    shortcode = json.loads(response.data)['shortcode']
    assert len(shortcode) == 6

def test_redirect_to_original_url(test_client):
    original_url = "https://www.example.com"
    shortcode = generate_shortcode()
    
    with app.app_context():
        short_url = URL(original_url=original_url, shortcode=shortcode)
        db.session.add(short_url)
        db.session.commit()

    response = test_client.get(f'/{shortcode}')
    assert response.status_code == 302
    assert response.location == original_url

def test_invalid_shortcode(test_client):
    response = test_client.get('/invalidshortcode')
    assert response.status_code == 404
