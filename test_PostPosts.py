import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_URL = f"{BASE_URL}/posts"  # Reusable URL for POST requests

# Reusable payload for all tests
DATA = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}



def test_successful_post_request():
    """Test to check if the server responds with HTTP status code 200 or 201."""
    response = requests.post(POSTS_URL, json=DATA)
    assert response.status_code in [200, 201], "POST request failed"


def test_post_response_time_is_less_than_500ms():
   
    """Test to check if the POST response time is less than 500ms.
       Sometime this test will fail because the server is slow "it tokes more than 500ms"
    """
    response = requests.post(POSTS_URL, json=DATA)
    assert response.elapsed.total_seconds() < 0.5, "POST response time is too slow"


def test_post_title_matches_input():
    """Test to check if the title in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("title") == DATA["title"], "Title does not match input"


def test_post_body_matches_input():
    """Test to check if the body in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("body") == DATA["body"], "Body does not match input"


def test_post_userid_matches_input():
    """Test to check if the userId in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA)
    json_data = response.json()
    assert json_data.get("userId") == DATA["userId"], "UserId does not match input"
