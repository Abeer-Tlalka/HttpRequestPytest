import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
GET_URL = f"{BASE_URL}/posts/1"  # Reusable URL for the GET request


def test_status_code_is_200():
    """Test to check if the response status code is 200."""
    response = requests.get(GET_URL)
    assert response.status_code == 200, "Status code is not 200"


def test_post_id_matches_requested_id():
    """Test to check if the post ID matches the requested ID."""
    response = requests.get(GET_URL)
    json_data = response.json()
    assert json_data['id'] == 1, "Post ID does not match the requested ID"


def test_post_title_is_not_empty():
    """Test to check if the post title is not empty."""
    response = requests.get(GET_URL)
    json_data = response.json()
    assert isinstance(json_data['title'], str) and json_data['title'], "Post title is empty"


def test_post_id_is_number_and_not_empty():
    """Test to check if the post ID is a number and not empty."""
    response = requests.get(GET_URL)
    json_data = response.json()
    assert isinstance(json_data['id'], int) and json_data['id'] is not None, "Post ID is not a valid number"


def test_post_body_is_not_empty():
    """Test to check if the post body is not empty."""
    response = requests.get(GET_URL)
    json_data = response.json()
    assert isinstance(json_data['body'], str) and json_data['body'], "Post body is empty"


def test_body_contains_expected_fields():
    """Test to check if the body contains the expected fields."""
    response = requests.get(GET_URL)
    json_data = response.json()
    expected_keys = ["userId", "id", "title", "body"]
    for key in expected_keys:
        assert key in json_data, f"Missing key: {key} in response body"
