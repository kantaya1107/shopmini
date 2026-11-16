def test_create_order_reduces_stock(client, products, customer_headers):
    payload = {"items": [{"product_id": 1, "quantity": 2}, {"product_id": 3, "quantity": 3}]}

    res = client.post("/api/orders", json=payload, headers=customer_headers)

    assert res.status_code == 201
    order = res.json()
    assert order["total_amount"] == 2490 * 2 + 250 * 3
    assert len(order["items"]) == 2
    assert client.get("/api/products/1").json()["stock"] == 8
    assert client.get("/api/products/3").json()["stock"] == 57


def test_insufficient_stock_rolls_back_everything(client, products, customer_headers):
    # สินค้า 3 มีพอ แต่สินค้า 2 มีไม่พอ: ต้องไม่ตัดสต็อกของสินค้า 3 ด้วย (All or Nothing)
    payload = {"items": [{"product_id": 3, "quantity": 1}, {"product_id": 2, "quantity": 6}]}

    res = client.post("/api/orders", json=payload, headers=customer_headers)

    assert res.status_code == 409
    assert res.json()["error"]["code"] == "INSUFFICIENT_STOCK"
    assert client.get("/api/products/3").json()["stock"] == 60
    assert client.get("/api/orders/me", headers=customer_headers).json() == []


def test_order_requires_login(client, products):
    res = client.post("/api/orders", json={"items": [{"product_id": 1, "quantity": 1}]})

    assert res.status_code == 401


def test_my_orders_only_returns_own_orders(client, products, customer_headers, admin_headers):
    client.post("/api/orders", json={"items": [{"product_id": 1, "quantity": 1}]}, headers=admin_headers)
    client.post("/api/orders", json={"items": [{"product_id": 3, "quantity": 1}]}, headers=customer_headers)

    res = client.get("/api/orders/me", headers=customer_headers)

    orders = res.json()
    assert len(orders) == 1
    assert orders[0]["items"][0]["product"]["id"] == 3