from app import app
import json

def test_collect_endpoint():
    with app.test_client() as client:
        response = client.get('/collect')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "data" in data
        assert "temperature" in data["data"]

def test_home_page_displays_data():
    with app.test_client() as client:
        # Collect a sample data
        client.get('/collect')
        response = client.get('/')
        assert response.status_code == 200
        html = response.data.decode('utf-8')
        assert "Weather Station Data" in html
        assert "Temp" in html or "Temperature" in html