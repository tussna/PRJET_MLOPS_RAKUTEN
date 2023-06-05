from fastapi.testclient import TestClient
import json

from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/home", headers = {"content-type": "html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Welcome to FastAPI Starter" in response.content
    response = client.get("app//static/css/style.css")
    assert response.status_code == 200

def test_page_about():
    response = client.get("/about", headers={"content-type": "html; charset=utf-8"})
    assert response.status_code == 200
    assert b"About" in response.content