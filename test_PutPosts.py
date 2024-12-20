import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
PUT_URL = f"{BASE_URL}/posts/1"  # Reusable URL for the PUT request

# Reusable payload for PUT request
DATA = {
    "id": 1,
    "title": "Updated Post Title",
    "body": "This is the updated content.",
    "userId": 1
}


def test_successful_put_request():
    """Test to check if the server responds with HTTP status code 200, 201, or 204."""
    response = requests.put(PUT_URL, json=DATA)
    assert response.status_code in [200, 201, 204], "PUT request failed"


def test_put_response_time_is_less_than_400ms():
    """Test to check if the PUT response time is less than 400ms."""
    response = requests.put(PUT_URL, json=DATA)
    assert response.elapsed.total_seconds() < 0.4, "PUT response time is too slow"


def test_put_title_is_updated_correctly():
    """Test to check if the title in the PUT response is updated correctly."""
    response = requests.put(PUT_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("title") == DATA["title"], "Title was not updated correctly"


def test_put_body_is_updated_correctly():
    """Test to check if the body in the PUT response is updated correctly."""
    response = requests.put(PUT_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("body") == DATA["body"], "Body was not updated correctly"


def test_put_userid_matches_input():
    """Test to check if the userId in the PUT response matches the input."""
    response = requests.put(PUT_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("userId") == DATA["userId"], "UserId does not match input"


def test_put_id_matches_input():
    """Test to check if the ID in the PUT response matches the input."""
    response = requests.put(PUT_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("id") == DATA["id"], "ID does not match input"
