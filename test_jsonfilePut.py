import pytest
import requests
import json

# Define the base URL
BASE_URL = "https://jsonplaceholder.typicode.com"  # Replace with your actual base URL

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

# Test 1: Status code is 200
def test_status_code_is_200():
    data = read_test_data()
    todo_id = 1  # Change this to the ID you want to test
    response = update_todo_data(todo_id, data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

# Test 2: Content-Type is JSON
def test_content_type_is_json():
    data = read_test_data()
    todo_id = 1  # Change this to the ID you want to test
    response = update_todo_data(todo_id, data)
    assert 'application/json' in response.headers['Content-Type'], "Expected Content-Type: application/json"

# Test 3: Updated data is returned correctly
def test_updated_data_is_returned_correctly():
    data = read_test_data()
    todo_id = 1  # Change this to the ID you want to test
    response = update_todo_data(todo_id, data)
    json_data = response.json()
    
    # Check the title and completed values match the input data
    assert json_data['title'] == data[0]['title'], f"Expected title: {data[0]['title']}, but got {json_data['title']}"
    assert json_data['completed'] == data[0]['completed'], f"Expected completed: {data[0]['completed']}, but got {json_data['completed']}"

