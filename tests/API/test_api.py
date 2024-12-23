import csv
import requests
import pytest
import json
BASE_URL = "https://jsonplaceholder.typicode.com"
HEADERS = {'Content-Type': 'application/json'}


DELETE_URL = f"{BASE_URL}/todos/60"  # Reusable URL for the DELETE request
GET_COMMENTS_URL = f"{BASE_URL}/posts/1/comments"  # Reusable URL
POSTS_URL = f"{BASE_URL}/posts"  # Reusable URL for POST requests
GET_POST_URL = f"{BASE_URL}/posts/1"  # Reusable URL for the GET request
PUT_URL = f"{BASE_URL}/posts/1"  # Reusable URL for the PUT request
JSON_FILE_URL=f"{BASE_URL}/todos"

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

# CSV file setup
CSV_FILE = 'results.csv'
FIELDNAMES = ['Request Type', 'Endpoint', 'Response Status', 'Result']

# Ensure the CSV file exists and has headers
with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
    writer.writeheader()


        
# Function to save test results to a CSV file
def save_test_result_to_csv(test_name, status, message):
    """Saves the test result to a CSV file."""
    with open('results.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([test_name, status, message])       
        
#------------------------------------
#--------Delete Todo------------------
#------------------------------------

# Test 1: Successful DELETE request
def test_successful_delete_todo_request():
    """Test to check if the server responds with HTTP status code 200, 202, or 204 for DELETE."""
    test_name = "test_successful_delete_todo_request"
    try:
        response = requests.delete(DELETE_URL)
        assert response.status_code in [200, 202, 204], "DELETE request failed"
        save_test_result_to_csv(test_name, "Pass", "DELETE request succeeded")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 2: DELETE response body is empty JSON
def test_delete_todo_response_body_is_empty_json():
    """Test to check if the DELETE response body is an empty JSON object."""
    test_name = "test_delete_todo_response_body_is_empty_json"
    try:
        response = requests.delete(DELETE_URL)
        assert response.text.strip() == "{}", "Response body is not an empty JSON object"
        save_test_result_to_csv(test_name, "Pass", "Response body is an empty JSON object")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))



#------------------------------------
#--------Get Comments 60------------------
#------------------------------------

# Test 1: Status code is 200
def test_status_GET_COMMENTS60_code_is_200():
    """Test to check if the status code is 200."""
    test_name = "test_status_GET_COMMENTS60_code_is_200"
    try:
        response = requests.get(GET_COMMENTS_URL)
        assert response.status_code == 200, "Status code is not 200"
        save_test_result_to_csv(test_name, "Pass", "Status code is 200")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 2: Response is in JSON format
def test__GET_COMMENTS60_response_is_json():
    """Test to check if the response is in JSON format."""
    test_name = "test__GET_COMMENTS60_response_is_json"
    try:
        response = requests.get(GET_COMMENTS_URL)
        response.json()  # Will raise ValueError if not JSON
        save_test_result_to_csv(test_name, "Pass", "Response is in JSON format")
    except ValueError:
        save_test_result_to_csv(test_name, "Fail", "Response is not in JSON format")

# Test 3: All comments belong to postId=1
def test_GET_COMMENTS60_all_comments_belong_to_post_1():
    """Test to check if all comments belong to postId=1."""
    test_name = "test_GET_COMMENTS60_all_comments_belong_to_post_1"
    try:
        response = requests.get(GET_COMMENTS_URL)
        data = response.json()
        for comment in data:
            assert comment.get("postId") == 1, "A comment does not belong to postId=1"
        save_test_result_to_csv(test_name, "Pass", "All comments belong to postId=1")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 4: Response time is less than 400ms
def test_response_time_is_less_than_400ms_GET_COMMENTS60():
    """Test to check if the response time is less than 400ms."""
    test_name = "test_response_time_is_less_than_400ms_GET_COMMENTS60"
    try:
        response = requests.get(GET_COMMENTS_URL)
        assert response.elapsed.total_seconds() < 0.4, "Response time is too slow"
        save_test_result_to_csv(test_name, "Pass", "Response time is less than 400ms")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 5: Required keys are present in each comment
def test_keys_are_present_in_each_comment60():
    """Test to check if all required keys are present in each comment."""
    test_name = "test_keys_are_present_in_each_comment60"
    try:
        response = requests.get(GET_COMMENTS_URL)
        data = response.json()
        for comment in data:
            assert "postId" in comment, "Key 'postId' is missing"
            assert "id" in comment, "Key 'id' is missing"
            assert "name" in comment, "Key 'name' is missing"
            assert "email" in comment, "Key 'email' is missing"
            assert "body" in comment, "Key 'body' is missing"
        save_test_result_to_csv(test_name, "Pass", "All required keys are present")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))



#------------------------------------
#--------Post Posts------------------
#------------------------------------
# Test 1: Server responds with HTTP status code 200 or 201
def test_successful_post_request_POTS_post():
    """Test to check if the server responds with HTTP status code 200 or 201."""
    test_name = "test_successful_post_request_POTS_post"
    try:
        response = requests.post(POSTS_URL, json=DATA_POST)
        assert response.status_code in [200, 201], "POST request failed"
        save_test_result_to_csv(test_name, "Pass", "POST request succeeded with status code 200 or 201")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 2: POST response time is less than 500ms
def test_POTS_postresponse_time_is_less_than_500ms():
    """Test to check if the POST response time is less than 500ms."""
    test_name = "test_POTS_postresponse_time_is_less_than_500ms"
    try:
        response = requests.post(POSTS_URL, json=DATA_POST)
        assert response.elapsed.total_seconds() < 0.5, "POST response time is too slow"
        save_test_result_to_csv(test_name, "Pass", "POST response time is less than 500ms")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 3: POST title matches input
def test_POTS_post_title_matches_input():
    """Test to check if the title in the POST response matches the input."""
    test_name = "test_POTS_post_title_matches_input"
    try:
        response = requests.post(POSTS_URL, json=DATA_POST)
        json_data = response.json()
        assert json_data.get("title") == DATA_POST["title"], "Title does not match input"
        save_test_result_to_csv(test_name, "Pass", "POST title matches input")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 4: POST body matches input
def test_POTS_post_body_matches_input():
    """Test to check if the body in the POST response matches the input."""
    test_name = "test_POTS_post_body_matches_input"
    try:
        response = requests.post(POSTS_URL, json=DATA_POST)
        json_data = response.json()
        assert json_data.get("body") == DATA_POST["body"], "Body does not match input"
        save_test_result_to_csv(test_name, "Pass", "POST body matches input")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 5: POST userId matches input
def test_POTS_post_userid_matches_input():
    """Test to check if the userId in the POST response matches the input."""
    test_name = "test_POTS_post_userid_matches_input"
    try:
        response = requests.post(POSTS_URL, json=DATA_POST)
        json_data = response.json()
        assert json_data.get("userId") == DATA_POST["userId"], "UserId does not match input"
        save_test_result_to_csv(test_name, "Pass", "POST userId matches input")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))


#------------------------------------
#--------Get Posts bY id------------------
#------------------------------------

# Test 1: Response status code is 200
def test_status_code_is_200_GET_post_by_id():
    """Test to check if the response status code is 200."""
    test_name = "test_status_code_is_200_GET_post_by_id"
    try:
        response = requests.get(GET_POST_URL)
        assert response.status_code == 200, "Status code is not 200"
        save_test_result_to_csv(test_name, "Pass", "Status code is 200")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 2: Post ID matches the requested ID
def test_post_id_matches_requested_id():
    """Test to check if the post ID matches the requested ID."""
    test_name = "test_post_id_matches_requested_id"
    try:
        response = requests.get(GET_POST_URL)
        json_data = response.json()
        assert json_data['id'] == 1, "Post ID does not match the requested ID"
        save_test_result_to_csv(test_name, "Pass", "Post ID matches the requested ID")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 3: Post title is not empty
def test_post_by_id_title_is_not_empty():
    """Test to check if the post title is not empty."""
    test_name = "test_post_by_id_title_is_not_empty"
    try:
        response = requests.get(GET_POST_URL)
        json_data = response.json()
        assert isinstance(json_data['title'], str) and json_data['title'], "Post title is empty"
        save_test_result_to_csv(test_name, "Pass", "Post title is not empty")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 4: Post ID is a number and not empty
def test_post_id_is_number_and_not_empty():
    """Test to check if the post ID is a number and not empty."""
    test_name = "test_post_id_is_number_and_not_empty"
    try:
        response = requests.get(GET_POST_URL)
        json_data = response.json()
        assert isinstance(json_data['id'], int) and json_data['id'] is not None, "Post ID is not a valid number"
        save_test_result_to_csv(test_name, "Pass", "Post ID is a valid number")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 5: Post body is not empty
def test_post_by_id_body_is_not_empty():
    """Test to check if the post body is not empty."""
    test_name = "test_post_by_id_body_is_not_empty"
    try:
        response = requests.get(GET_POST_URL)
        json_data = response.json()
        assert isinstance(json_data['body'], str) and json_data['body'], "Post body is empty"
        save_test_result_to_csv(test_name, "Pass", "Post body is not empty")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 6: Body contains the expected fields
def test_body_by_id_contains_expected_fields():
    """Test to check if the body contains the expected fields."""
    test_name = "test_body_by_id_contains_expected_fields"
    try:
        response = requests.get(GET_POST_URL)
        json_data = response.json()
        expected_keys = ["userId", "id", "title", "body"]
        for key in expected_keys:
            assert key in json_data, f"Missing key: {key} in response body"
        save_test_result_to_csv(test_name, "Pass", "Body contains all expected fields")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

#------------------------------------
#--------Put Posts Data------------------
#------------------------------------
# Test 1: Check server responds with appropriate status code
def test_successful_put_post_request():
    """Test to check if the server responds with HTTP status code 200, 201, or 204."""
    test_name = "test_successful_put_post_request"
    try:
        response = requests.put(PUT_URL, json=PUT_POST_DATA)
        assert response.status_code in [200, 201, 204], "PUT request failed"
        save_test_result_to_csv(test_name, "Pass", "PUT request successful")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 2: Check if title is updated correctly
def test_put_post_title_is_updated_correctly():
    """Test to check if the title in the PUT response is updated correctly."""
    test_name = "test_put_post_title_is_updated_correctly"
    try:
        response = requests.put(PUT_URL, json=PUT_POST_DATA)
        json_data = response.json()
        assert json_data.get("title") == PUT_POST_DATA["title"], "Title was not updated correctly"
        save_test_result_to_csv(test_name, "Pass", "Title updated correctly")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 3: Check if body is updated correctly
def test_put_post_body_is_updated_correctly():
    """Test to check if the body in the PUT response is updated correctly."""
    test_name = "test_put_post_body_is_updated_correctly"
    try:
        response = requests.put(PUT_URL, json=PUT_POST_DATA)
        json_data = response.json()
        assert json_data.get("body") == PUT_POST_DATA["body"], "Body was not updated correctly"
        save_test_result_to_csv(test_name, "Pass", "Body updated correctly")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 4: Check if userId matches the input
def test_put_post_userid_matches_input():
    """Test to check if the userId in the PUT response matches the input."""
    test_name = "test_put_post_userid_matches_input"
    try:
        response = requests.put(PUT_URL, json=PUT_POST_DATA)
        json_data = response.json()
        assert json_data.get("userId") == PUT_POST_DATA["userId"], "UserId does not match input"
        save_test_result_to_csv(test_name, "Pass", "UserId matches input")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# Test 5: Check if ID matches the input
def test_put_post_id_matches_input():
    """Test to check if the ID in the PUT response matches the input."""
    test_name = "test_put_post_id_matches_input"
    try:
        response = requests.put(PUT_URL, json=PUT_POST_DATA)
        json_data = response.json()
        assert json_data.get("id") == PUT_POST_DATA["id"], "ID does not match input"
        save_test_result_to_csv(test_name, "Pass", "ID matches input")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))
        
#------------------------------------
#--------JSON File's Tests-----------
#------------------------------------


#----------POST-----------

# Read data from the test_data.json file
def read_test_data():
    with open('test_data.json', 'r') as file:
        return json.load(file)

def test_status_code_JSONFILE():
    test_name = "test_status_code_JSONFILE"
    try:
        data = read_test_data()
        response = requests.post(JSON_FILE_URL, json=data[1], headers=HEADERS)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        save_test_result_to_csv(test_name, "Pass", "Status code is 201")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

def test_content_type_JSONFILE():
    test_name = "test_content_type_JSONFILE"
    try:
        data = read_test_data()
        response = requests.post(JSON_FILE_URL, json=data[1], headers=HEADERS)
        assert 'application/json' in response.headers['Content-Type'], "Content-Type is not application/json"
        save_test_result_to_csv(test_name, "Pass", "Content-Type is application/json")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

def test_response_json_schema_JSONFILE():
    test_name = "test_response_json_schema_JSONFILE"
    try:
        data = read_test_data()
        response = requests.post(JSON_FILE_URL, json=data[1], headers=HEADERS)
        json_data = response.json()
        required_fields = ["id", "userId", "title", "completed"]
        for field in required_fields:
            assert field in json_data, f"Response does not contain '{field}'"
        save_test_result_to_csv(test_name, "Pass", "Response matches JSON schema")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

def test_id_returned_JSONFILE():
    test_name = "test_id_returned_JSONFILE"
    try:
        data = read_test_data()
        response = requests.post(JSON_FILE_URL, json=data[1], headers=HEADERS)
        json_data = response.json()
        assert "id" in json_data, "Response does not contain 'id'"
        save_test_result_to_csv(test_name, "Pass", "ID is returned in the response")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

# -------------- PUT TESTS -----------------
def update_todo_data_JSONFILE(todo_id, data):
    url = f"{BASE_URL}/todos/{todo_id}"
    response = requests.put(url, json=data, headers=HEADERS)
    return response

def test_status_code_is_200():
    test_name = "test_status_code_is_200"
    try:
        data = read_test_data()
        todo_id = 1  # Replace with a valid ID
        response = update_todo_data_JSONFILE(todo_id, data[0])
        assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
        save_test_result_to_csv(test_name, "Pass", "Status code is 200")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))

def test_content_type_is_json():
    test_name = "test_content_type_is_json"
    try:
        data = read_test_data()
        todo_id = 1  # Replace with a valid ID
        response = update_todo_data_JSONFILE(todo_id, data[0])
        assert 'application/json' in response.headers['Content-Type'], "Expected Content-Type: application/json"
        save_test_result_to_csv(test_name, "Pass", "Content-Type is application/json")
    except AssertionError as e:
        save_test_result_to_csv(test_name, "Fail", str(e))
