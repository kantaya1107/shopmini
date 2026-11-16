def test_list_products_returns_page(client, products):
    res = client.get("/api/products")

    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 3
    assert body["page"] == 1
    assert len(body["items"]) == 3


def test_filter_by_category_and_search(client, products):
    res = client.get("/api/products", params={"category": "audio", "search": "หูฟัง"})

    names = [p["name"] for p in res.json()["items"]]
    assert names == ["หูฟังบลูทูธ ANC"]


def test_sort_price_ascending(client, products):
    res = client.get("/api/products", params={"sort": "price_asc"})

    prices = [p["price"] for p in res.json()["items"]]
    assert prices == sorted(prices)


def test_pagination_metadata(client, products):
    res = client.get("/api/products", params={"page": 2, "size": 2})

    body = res.json()
    assert body["pages"] == 2
    assert len(body["items"]) == 1


def test_get_product_not_found(client):
    res = client.get("/api/products/9999")

    assert res.status_code == 404
    assert res.json()["error"]["code"] == "NOT_FOUND"


def test_create_product_requires_login(client, products):
    res = client.post("/api/products", json={"name": "ใหม่", "price": 100, "category_id": 1})

    assert res.status_code == 401


def test_customer_cannot_create_product(client, products, customer_headers):
    res = client.post(
        "/api/products", json={"name": "ใหม่", "price": 100, "category_id": 1}, headers=customer_headers
    )

    assert res.status_code == 403


def test_admin_can_create_product(client, products, admin_headers):
    payload = {"name": "เว็บแคม Full HD", "price": 1290, "stock": 5, "category_id": 1}

    res = client.post("/api/products", json=payload, headers=admin_headers)

    assert res.status_code == 201
    data = res.json()
    assert data["id"] > 0
    assert data["price"] == 1290
    assert data["category"]["slug"] == "audio"


def test_create_product_validation_error(client, products, admin_headers):
    res = client.post(
        "/api/products", json={"name": "A", "price": -1, "category_id": 1}, headers=admin_headers
    )

    assert res.status_code == 422
    fields = {d["field"] for d in res.json()["error"]["details"]}
    assert fields == {"name", "price"}


def test_admin_can_update_and_delete(client, products, admin_headers):
    res = client.patch("/api/products/1", json={"stock": 99}, headers=admin_headers)
    assert res.status_code == 200
    assert res.json()["stock"] == 99

    res = client.delete("/api/products/1", headers=admin_headers)
    assert res.status_code == 204
    assert client.get("/api/products/1").status_code == 404

# คำสั่งรันเทส
# pytest tests/test_products.py -v