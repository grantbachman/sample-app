from app import app


def test_root():
    test_app = app.test_client()
    response = test_app.get('/')
    assert b'Hello, World!' in response.data
