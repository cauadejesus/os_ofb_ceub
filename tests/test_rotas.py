def test_contracts_exige_login(client):
    resp = client.get("/contracts")

    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]

def test_login_valido_abre_painel(client):
    resp = client.post("/login", data={
        "username": "gestor",
        "password": "Gestor@123"},
        follow_redirects=True)
    assert resp.status_code == 200