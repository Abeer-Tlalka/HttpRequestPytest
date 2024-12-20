import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
COMMENTS_URL = f"{BASE_URL}/posts/1/comments"  # Reusable URL


def test_status_code_is_200():
    """Test to check if the status code is 200."""
    response = requests.get(COMMENTS_URL)
    assert response.status_code == 200, "Status code is not 200"


def test_response_is_json():
    """Test to check if the response is in JSON format."""
    response = requests.get(COMMENTS_URL)
    try:
        response.json()
    except ValueError:
        assert False, "Response is not in JSON format"


def test_all_comments_belong_to_post_1():
    """Test to check if all comments belong to postId=1."""
    response = requests.get(COMMENTS_URL)
    data = response.json()
    for comment in data:
        assert comment.get("postId") == 1, "A comment does not belong to postId=1"


def test_response_time_is_less_than_400ms():
    """Test to check if the response time is less than 400ms."""
    response = requests.get(COMMENTS_URL)
    assert response.elapsed.total_seconds() < 0.4, "Response time is too slow"


def test_keys_are_present_in_each_comment():
    """Test to check if all required keys are present in each comment."""
    response = requests.get(COMMENTS_URL)
    data = response.json()
    for comment in data:
        assert "postId" in comment, "Key 'postId' is missing"
        assert "id" in comment, "Key 'id' is missing"
        assert "name" in comment, "Key 'name' is missing"
        assert "email" in comment, "Key 'email' is missing"
        assert "body" in comment, "Key 'body' is missing"
