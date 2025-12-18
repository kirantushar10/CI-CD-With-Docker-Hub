## Any File/Folder that begins with 'test' in its name will be considered by pytest.

from app import app

def test_home():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b"Hello, World!"