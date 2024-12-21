import unittest
from app import app

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.token = "secure-token"

    def test_add_book(self):
        response = self.client.post('/books', json={"title": "Book 1", "author": "Author 1"}, headers={"Authorization": self.token})
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        self.client.post('/books', json={"title": "Book 1", "author": "Author 1"}, headers={"Authorization": self.token})
        response = self.client.get('/books', headers={"Authorization": self.token})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
