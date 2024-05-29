import requests
import json
from test_runner import test_functions

BASE_URL = "http://localhost:5000"

def test_home():
    """Test the home route of the API."""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.text == "Welcome to the Flask API!"

def test_get_data_initial():
    """Test the data route of the API when no users are added."""
    response = requests.get(f"{BASE_URL}/data")
    assert response.status_code == 200
    assert response.json() == []

def test_add_user():
    """Test adding a user to the API."""
    user_data = {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=user_data)
    assert response.status_code == 201
    assert response.json() == {
        "message": "User added",
        "user": user_data
    }

def test_get_data_after_adding_user():
    """Test the data route of the API after adding a user."""
    response = requests.get(f"{BASE_URL}/data")
    assert response.status_code == 200
    assert response.json() == ["john"]

def test_get_user():
    """Test getting a user from the API."""
    response = requests.get(f"{BASE_URL}/users/john")
    assert response.status_code == 200
    assert response.json() == {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }

def test_get_nonexistent_user():
    """Test getting a user that does not exist."""
    response = requests.get(f"{BASE_URL}/users/doesnotexist")
    assert response.status_code == 404
    assert response.json() == {"error": "User not found"}

def test_status():
    """Test the status route of the API."""
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.text == "OK"

def test_add_user_without_username():
    """Test adding a user without a username."""
    user_data = {
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=user_data)
    assert response.status_code == 400
    assert response.json() == {"error": "Username is required"}

def test_add_user_duplicate_username():
    """Test adding a user with a duplicate username."""
    user_data = {
        "username": "john",
        "name": "Johnny",
        "age": 40,
        "city": "Los Angeles"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=user_data)
    assert response.status_code == 201  # Assuming the API allows updates, otherwise this test needs to be adjusted
    assert response.json() == {
        "message": "User added",
        "user": user_data
    }


if __name__ == "__main__":
    test_functions([test_home,
    test_get_data_initial,
    test_add_user,
    test_get_data_after_adding_user,
    test_get_user,
    test_get_nonexistent_user,
    test_status,
    test_add_user_without_username,
    test_add_user_duplicate_username])
