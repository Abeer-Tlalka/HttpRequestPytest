# API Testing with pytest

This project contains automated tests for the **JSONPlaceholder API** using the `pytest` framework. JSONPlaceholder is a free fake online REST API used for testing and prototyping.

## Project Overview

The tests in this repository focus on validating the **POST** and **PUT** API endpoints provided by JSONPlaceholder. These tests ensure that the API responds as expected, with proper status codes, content types, and JSON schema compliance.

### API Endpoints Tested

- **POST /todos**: This endpoint is used to create a new Todo item.
- **PUT /todos/{id}**: This endpoint updates an existing Todo item by its ID.

## Test Files

The tests are organized into two main groups:

1. **POST Tests**: Tests related to creating a new Todo item.
    - **test_status_code_JSONFILE**: Validates that the API returns a `201 Created` status code when posting data.
    - **test_content_type_JSONFILE**: Validates that the `Content-Type` in the response is `application/json`.
    - **test_response_json_schema_JSONFILE**: Validates that the response contains required fields like `id`, `userId`, `title`, and `completed`.
    - **test_id_returned_JSONFILE**: Validates that the response contains an `id` field after posting data.

2. **PUT Tests**: Tests related to updating an existing Todo item.
    - **test_status_code_is_200**: Validates that the API returns a `200 OK` status code when updating a Todo item.
    - **test_content_type_is_json**: Validates that the `Content-Type` in the response is `application/json` when updating a Todo item.

## Test Data

Test data for the API requests is read from a **JSON file** (`test_data.json`). This file contains sample data used in both POST and PUT requests. It includes:
- A list of sample Todo items for testing the `POST /todos` endpoint.
- Data for updating existing Todo items for testing the `PUT /todos/{id}` endpoint.

## Prerequisites

To run the tests, ensure you have the following dependencies installed:

- `requests` for making HTTP requests to the API.
- `pytest` for running the tests and assertions.

You can install the dependencies using `pip`:

```bash
pip install requests pytest
