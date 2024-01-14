import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app as flask_app
from flask import Flask
from datetime import datetime
import re
import pytest

@pytest.fixture
def app():
    """Fixture para crear una instancia de la aplicación Flask para pruebas."""
    app = flask_app
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    """Fixture para crear un cliente de prueba para la aplicación Flask."""
    return app.test_client()

def test_index_route(client):
    """Verifica que la ruta raíz '/' devuelve un código de respuesta 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_index_route_content(client):
    """Verifica que la ruta raíz contiene el mensaje de bienvenida en la respuesta."""
    response = client.get('/')
    assert b'\xc2\xa1Bienvenidos!' in response.data

def test_index_route_date_time(client):
    """Verifica que la ruta raíz contiene la fecha y hora actual en el formato esperado."""
    response = client.get('/')
    assert re.search(rb'Fecha y Hora Actuales: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', response.data)

def test_template_rendering(client):
    """Verifica que la plantilla 'index.html' se renderiza correctamente."""
    response = client.get('/')
    assert b'<!DOCTYPE html>' in response.data
    assert b'<h1>\xc2\xa1Bienvenidos!</h1>' in response.data