import json
import pytest
from app.services import add_short_url
from app import create_app, db
from app.models import URL
from app.utils import generate_shortcode

app = create_app()

# Definir un fixture para el cliente de prueba
@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as test_client:
        # Crear las tablas de la base de datos dentro del contexto de la aplicación
        with app.app_context():
            db.create_all()
        # Entregar al cliente de prueba para que las pruebas lo usen
        yield test_client
        # Dropear las tablas de la base de datos dentro del contexto de la aplicación
        with app.app_context():
            db.drop_all()


# Probar el endpoint para acortar URL
def test_shorten_url(test_client):
    original_url = "https://www.example.com"
    response = test_client.post('/shorten', data=json.dumps({"url": original_url}), content_type='application/json')

    # Verificar que la respuesta tenga un código de estado de 200
    assert response.status_code == 200
    # Comprobar que el shortcode tenga una longitud de 6
    shortcode = json.loads(response.data)['shortcode']
    assert len(shortcode) == 6

# Probar el endpoint para redirigir a la URL original
def test_redirect_to_original_url(test_client):
    original_url = "https://www.example.com"
    shortcode = generate_shortcode()
    
    # Agregar un objeto URL a la base de datos
    with app.app_context():
        short_url = URL(original_url=original_url, shortcode=shortcode)
        db.session.add(short_url)
        db.session.commit()

    # Comprobar que el endpoint redirige correctamente
    response = test_client.get(f'/{shortcode}')
    assert response.status_code == 302
    assert response.location == original_url

# Pruebe que el punto final devuelve un código de estado 404 para un código abreviado no válido
def test_invalid_shortcode(test_client):
    response = test_client.get('/invalidshortcode')
    assert response.status_code == 404
