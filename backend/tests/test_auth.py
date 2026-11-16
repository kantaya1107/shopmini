NEW_USER = {"email": "somchai@example.com", "full_name": "สมชาย ใจดี", "password": "Passw0rd!"}


def test_register_success(client):
    res = client.post("/api/auth/register", json=NEW_USER)

    assert res.status_code == 201
    body = res.json()
    assert body["email"] == NEW_USER["email"]
    assert body["role"] == "customer"
    assert "password" not in body and "hashed_password" not in body


def test_register_duplicate_email(client):
    client.post("/api/auth/register", json=NEW_USER)

    res = client.post("/api/auth/register", json=NEW_USER)

    assert res.status_code == 409


def test_password_is_hashed_in_database(client, db):
    from app.models import User

    client.post("/api/auth/register", json=NEW_USER)

    user = db.query(User).filter_by(email=NEW_USER["email"]).one()
    assert user.hashed_password != NEW_USER["password"]
    assert user.hashed_password.startswith("$2b$")


def test_login_and_get_me(client):
    client.post("/api/auth/register", json=NEW_USER)

    res = client.post(
        "/api/auth/login", data={"username": NEW_USER["email"], "password": NEW_USER["password"]}
    )
    assert res.status_code == 200
    token = res.json()["access_token"]

    me = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    assert me.json()["full_name"] == NEW_USER["full_name"]


def test_login_wrong_password(client):
    client.post("/api/auth/register", json=NEW_USER)

    res = client.post("/api/auth/login", data={"username": NEW_USER["email"], "password": "wrong"})

    assert res.status_code == 401


def test_me_without_token_returns_401(client):
    res = client.get("/api/auth/me")

    assert res.status_code == 401
    assert res.headers["www-authenticate"] == "Bearer"


def test_me_with_invalid_token_returns_401(client):
    res = client.get("/api/auth/me", headers={"Authorization": "Bearer not-a-real-token"})

    assert res.status_code == 401