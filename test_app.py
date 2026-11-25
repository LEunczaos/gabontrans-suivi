from app import app

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_get_colis_success():
    client = app.test_client()
    response = client.get("/colis/GT-1001")
    assert response.status_code == 200
    assert response.get_json() ["client"] == "SOTELGAB"

def test_get_colis_not_found():
    client = app.test_client()
    response = client.get("/colis/GT-9999")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Colis not found"}