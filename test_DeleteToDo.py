import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
DELETE_URL = f"{BASE_URL}/todos/60"  # Reusable URL for the DELETE request


def test_successful_delete_request():
    """Test to check if the server responds with HTTP status code 200, 202, or 204 for DELETE."""
    response = requests.delete(DELETE_URL)
    assert response.status_code in [200, 202, 204], "DELETE request failed"


def test_delete_response_body_is_empty_json():
    """Test to check if the DELETE response body is an empty JSON object."""
    response = requests.delete(DELETE_URL)
    assert response.text.strip() == "{}", "Response body is not an empty JSON object"
