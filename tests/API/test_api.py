import requests
import pytest
import json
BASE_URL = "https://jsonplaceholder.typicode.com"

DELETE_URL = f"{BASE_URL}/todos/60"  # Reusable URL for the DELETE request
GET_COMMENTS_URL = f"{BASE_URL}/posts/1/comments"  # Reusable URL
POSTS_URL = f"{BASE_URL}/posts"  # Reusable URL for POST requests
GET_POST_URL = f"{BASE_URL}/posts/1"  # Reusable URL for the GET request
PUT_URL = f"{BASE_URL}/posts/1"  # Reusable URL for the PUT request

# Reusable payload for PUT request
PUT_POST_DATA = {
    "id": 1,
    "title": "Updated Post Title",
    "body": "This is the updated content.",
    "userId": 1
}

DATA_POST = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}


#------------------------------------
#--------Delete Todo------------------
#------------------------------------
def test_successful_delete_todio_request():
    """Test to check if the server responds with HTTP status code 200, 202, or 204 for DELETE."""
    response = requests.delete(DELETE_URL)
    assert response.status_code in [200, 202, 204], "DELETE request failed"


def test_delete_todo_response_body_is_empty_json():
    """Test to check if the DELETE response body is an empty JSON object."""
    response = requests.delete(DELETE_URL)
    assert response.text.strip() == "{}", "Response body is not an empty JSON object"


#------------------------------------
#--------Get Comments 60------------------
#------------------------------------


def test_status_GET_COMMENTS60_code_is_200():
    """Test to check if the status code is 200."""
    response = requests.get(GET_COMMENTS_URL)
    assert response.status_code == 200, "Status code is not 200"


def test__GET_COMMENTS60_response_is_json():
    """Test to check if the response is in JSON format."""
    response = requests.get(GET_COMMENTS_URL)
    try:
        response.json()
    except ValueError:
        assert False, "Response is not in JSON format"


def test_GET_COMMENTS60_all_comments_belong_to_post_1():
    """Test to check if all comments belong to postId=1."""
    response = requests.get(GET_COMMENTS_URL)
    data = response.json()
    for comment in data:
        assert comment.get("postId") == 1, "A comment does not belong to postId=1"

#NOTE: This test will fail because the server is slow, sometime it's took more than 400ms
def test_response_time_is_less_than_400ms_GET_COMMENTS60():
    """Test to check if the response time is less than 400ms."""
    response = requests.get(GET_COMMENTS_URL)
    assert response.elapsed.total_seconds() < 0.4, "Response time is too slow"


def test_keys_are_present_in_each_comment60():
    """Test to check if all required keys are present in each comment."""
    response = requests.get(GET_COMMENTS_URL)
    data = response.json()
    for comment in data:
        assert "postId" in comment, "Key 'postId' is missing"
        assert "id" in comment, "Key 'id' is missing"
        assert "name" in comment, "Key 'name' is missing"
        assert "email" in comment, "Key 'email' is missing"
        assert "body" in comment, "Key 'body' is missing"



#------------------------------------
#--------Post Posts------------------
#------------------------------------


def test_successful_post_request_POTS_post():
    """Test to check if the server responds with HTTP status code 200 or 201."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    assert response.status_code in [200, 201], "POST request failed"

#NOTE: This test will fail because the server is slow, sometime it's took more than 500ms
def test_POTS_postresponse_time_is_less_than_500ms():
   
    """Test to check if the POST response time is less than 500ms.
       Sometime this test will fail because the server is slow "it tokes more than 500ms"
    """
    response = requests.post(POSTS_URL, json=DATA_POST)
    assert response.elapsed.total_seconds() < 0.5, "POST response time is too slow"


def test_POTS_post_title_matches_input():
    """Test to check if the title in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    json_data = response.json()
    assert json_data.get("title") == DATA_POST["title"], "Title does not match input"


def test_POTS_post_body_matches_input():
    """Test to check if the body in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    json_data = response.json()
    assert json_data.get("body") == DATA_POST["body"], "Body does not match input"


def test_POTS_post_userid_matches_input():
    """Test to check if the userId in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    json_data = response.json()
    assert json_data.get("userId") == DATA_POST["userId"], "UserId does not match input"

#------------------------------------
#--------Get Posts bY id------------------
#------------------------------------



def test_status_code_is_200_GET_post_by_id():
    """Test to check if the response status code is 200."""
    response = requests.get(GET_POST_URL)
    assert response.status_code == 200, "Status code is not 200"


def test_post_id_matches_requested_id():
    """Test to check if the post ID matches the requested ID."""
    response = requests.get(GET_POST_URL)
    json_data = response.json()
    assert json_data['id'] == 1, "Post ID does not match the requested ID"


def test_post_by_id_title_is_not_empty():
    """Test to check if the post title is not empty."""
    response = requests.get(GET_POST_URL)
    json_data = response.json()
    assert isinstance(json_data['title'], str) and json_data['title'], "Post title is empty"


def test_post_id_is_number_and_not_empty():
    """Test to check if the post ID is a number and not empty."""
    response = requests.get(GET_POST_URL)
    json_data = response.json()
    assert isinstance(json_data['id'], int) and json_data['id'] is not None, "Post ID is not a valid number"


def test_post_by_id_body_is_not_empty():
    """Test to check if the post body is not empty."""
    response = requests.get(GET_POST_URL)
    json_data = response.json()
    assert isinstance(json_data['body'], str) and json_data['body'], "Post body is empty"


def test_body_by_id_contains_expected_fields():
    """Test to check if the body contains the expected fields."""
    response = requests.get(GET_POST_URL)
    json_data = response.json()
    expected_keys = ["userId", "id", "title", "body"]
    for key in expected_keys:
        assert key in json_data, f"Missing key: {key} in response body"


#------------------------------------
#--------Put Posts Data------------------
#------------------------------------


def test_successful_put_post_request():
    """Test to check if the server responds with HTTP status code 200, 201, or 204."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    assert response.status_code in [200, 201, 204], "PUT request failed"

#NOTE: This test will fail because the server is slow
def test_put_post_response_time_is_less_than_400ms():
    """Test to check if the PUT response time is less than 400ms."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    assert response.elapsed.total_seconds() < 0.4, "PUT response time is too slow"


def test_put_post_title_is_updated_correctly():
    """Test to check if the title in the PUT response is updated correctly."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("title") == PUT_POST_DATA["title"], "Title was not updated correctly"


def test_put_post_body_is_updated_correctly():
    """Test to check if the body in the PUT response is updated correctly."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("body") == PUT_POST_DATA["body"], "Body was not updated correctly"


def test_put_post_userid_matches_input():
    """Test to check if the userId in the PUT response matches the input."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("userId") == PUT_POST_DATA["userId"], "UserId does not match input"


def test_put_post_id_matches_input():
    """Test to check if the ID in the PUT response matches the input."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("id") == PUT_POST_DATA["id"], "ID does not match input"



#------------------------------------
#--------JSON File's Tests-----------
#------------------------------------


# Load data from JSON file
def read_test_data():
    with open('test_data.json', 'r') as file:
        return json.load(file)

# This function will perform the PUT request with the provided ID
def update_todo_data(todo_id, data):
    url = f"{BASE_URL}/todos/{todo_id}"
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=data, headers=headers)
    return response


def test_JSON_File_status_code_is_200():
    data = read_test_data()
    todo_id = 1  
    response = update_todo_data(todo_id, data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

def test_JSON_File_content_type_is_json():
    data = read_test_data()
    todo_id = 1   
    response = update_todo_data(todo_id, data)
    assert 'application/json' in response.headers['Content-Type'], "Expected Content-Type: application/json"

# def test_JSON_File_title_data_is_returned_correctly():
#     data = read_test_data()
#     todo_id = 1  
#     response = update_todo_data(todo_id, data)
#     json_data = response.json()
    
#     assert json_data['title'] == data[0]['title'], f"Expected title: {data[0]['title']}, but got {json_data['title']}"


# Test function to update a post and verify the response
def test_JSON_File_title_data_is_returned_correctly(BASE_URL):
    """
    Test to update a post using all fields from test_data.json
    and verify the response matches the data.
    """
    # Read data from test_data.json
    test_data = read_test_data()
    todo_id = 1  # ID of the post to update

    # Use the first entry from the test data
    payload = test_data[0]

    response = requests.put(f"{BASE_URL}/posts/{todo_id}", json=payload)
    json_data = response.json()

    # Assertions
    assert response.status_code == 200, "Failed to update the todo item"
    assert json_data.get("id") == todo_id, f"Expected ID: {todo_id}, but got {json_data.get('id')}"
    for key in payload:
        assert json_data.get(key) == payload[key], f"Expected {key}: {payload[key]}, but got {json_data.get(key)}"




def test_JSON_File_completed_data_is_returned_correctly():
    data = read_test_data()
    todo_id = 1  
    response = update_todo_data(todo_id, data)
    json_data = response.json()
    
    assert json_data['completed'] == data[0]['completed'], f"Expected completed: {data[0]['completed']}, but got {json_data['completed']}"
