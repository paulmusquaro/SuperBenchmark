from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_average_results():
    response = client.get("/results/average")
    assert response.status_code == 200
    data = response.json()
    assert "avg_token_count" in data


def test_get_average_results_within_window():
    response = client.get("/results/average/2024-06-01T00:00:00/2024-06-01T23:59:59")
    assert response.status_code == 200
    data = response.json()
    assert "avg_token_count" in data
