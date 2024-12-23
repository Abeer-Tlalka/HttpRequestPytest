import requests
import json

# Base URL
BASE_URL = "https://jsonplaceholder.typicode.com"
POST_URL = f"{BASE_URL}/todos"  # Reusable URL for the POST request

# Read data from the test_data.json file
def read_test_data():
    with open('test_data.json', 'r') as file:
        return json.load(file)

# Function to test if the status code is 201
def test_status_code():
    data = read_test_data()
    response = requests.post(POST_URL, json=data)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

# Function to test if Content-Type is JSON
def test_content_type():
    data = read_test_data()
    response = requests.post(POST_URL, json=data)
    assert 'application/json' in response.headers['Content-Type'], "Content-Type is not application/json"

# Function to test if the response matches the expected JSON schema
def test_response_json_schema():
    data = read_test_data()
    response = requests.post(POST_URL, json=data[1])
    json_data = response.json()
    assert "id" in json_data, "Response does not contain 'id'"
    assert "userId" in json_data, "Response does not contain 'userId'"
    assert "title" in json_data, "Response does not contain 'title'"
    assert "completed" in json_data, "Response does not contain 'completed'"

# Function to test if the title matches the input value
def test_title_match():
    data = read_test_data()
    response = requests.post(POST_URL, json=data)
    json_data = response.json()
    assert json_data['title'] == data['title'], "Title in response does not match the input title"

# Function to test if ID is returned in the response
def test_id_returned():
    data = read_test_data()
    response = requests.post(POST_URL, json=data)
    json_data = response.json()
    assert "id" in json_data, "Response does not contain 'id'"

