#!/usr/bin/python3
"""Unittests for TestThree Class
"""
import unittest
import requests


class TestThree(unittest.TestCase):
    """Test functions for TestThree Class
    """
    base_url = 'http://localhost:8000'

    def test_api_root(self):
        """Test if root endpoint returns correct content."""
        response = requests.get(self.base_url, timeout=5)
        assert response.status_code == 200, "Root endpoint should return status 200"
        assert response.text == "Hello, this is a simple API!", "Root endpoint returned incorrect content"

    def test_api_data(self):
        """Test if data endpoint returns correct data."""
        response = requests.get(f'{self.base_url}/data', timeout=5)
        assert response.status_code == 200, "Data endpoint should return status 200"
        assert response.headers['Content-Type'] == 'application/json', "Data endpoint should return JSON content type"
        data = response.json()
        assert data == {"name": "John", "age": 30, "city": "New York"}, "Data endpoint returned incorrect data"

    def test_api_status(self):
        """Test if status endpoint returns correct status."""
        response = requests.get(f'{self.base_url}/status', timeout=5)
        assert response.status_code == 200, "Status endpoint should return status 200"
        assert response.text == "OK", "Status endpoint returned incorrect content"

    def test_api_undefined_endpoint(self):
        """Test if undefined endpoint returns correct status."""
        response = requests.get(f'{self.base_url}/undefined', timeout=5)
        assert response.status_code == 404, "Undefined endpoint should return status 404"
        assert response.text == "404 Not Found", "Undefined endpoint returned incorrect content"

if __name__ == '__main__':
    unittest.main()