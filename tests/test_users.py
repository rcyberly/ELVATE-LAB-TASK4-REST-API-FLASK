import json
from app import create_app

def test_create_user():
    app = create_app()
    client = app.test_client()
    res = client.post("/api/users", json={"name": "R", "email": "r@example.com"})
    assert res.status_code == 201
    body = res.get_json()
    assert body["email"] == "r@example.com"

def test_get_users():
    app = create_app()
    client = app.test_client()
    client.post("/api/users", json={"name": "A", "email": "a@example.com"})
    res = client.get("/api/users")
    assert res.status_code == 200
    assert len(res.get_json()["items"]) >= 1
