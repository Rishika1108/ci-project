"""
Unit tests for the service.
"""
import unittest
from service.routes import app, add_numbers


class TestRoutes(unittest.TestCase):
    """Test cases for the Flask routes."""

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        """It should return a welcome message on the root route."""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Welcome", resp.data)

    def test_health(self):
        """It should return OK on the health route."""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"OK", resp.data)

    def test_add_numbers(self):
        """It should correctly add two numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
