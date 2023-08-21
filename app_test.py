import requests
import pytest

# Assuming you have the service URL configured
SERVICE_URL = "https://www.fotor.com/images/create"

@pytest.mark.parametrize("text", ["Hello", "World", "FastAPI"])
def test_image_generation(text):
    response = requests.get(f"{SERVICE_URL}/convert_text_to_image/{text}")
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("image/")
    # You can add more assertions to check image quality or content if needed

def test_edge_case():
    # Test an edge case or potentially problematic input
    response = requests.get(f"{SERVICE_URL}/convert_text_to_image/")
    assert response.status_code != 200  # Expect a non-200 status code

def test_erroneous_input():
    # Test with erroneous input that may cause issues
    response = requests.get(f"{SERVICE_URL}/convert_text_to_image/?text=Invalid%20Input")
    assert response.status_code != 200  # Expect a non-200 status code

def test_health_endpoint():
    response = requests.get(f"{SERVICE_URL}/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
