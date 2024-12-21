import unittest
from app import app

class TestMembers(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.token = "secure-token"

    def test_add_member(self):
        """Test adding a new member"""
        response = self.client.post(
            '/members',
            json={"name": "John Doe"},
            headers={"Authorization": self.token}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())
        self.assertEqual(response.get_json()["name"], "John Doe")

    def test_get_all_members(self):
        """Test retrieving all members"""
        # Add a member first
        self.client.post(
            '/members',
            json={"name": "Jane Doe"},
            headers={"Authorization": self.token}
        )

        response = self.client.get(
            '/members',
            headers={"Authorization": self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)
        self.assertGreater(len(response.get_json()), 0)

    def test_get_single_member(self):
        """Test retrieving a single member by ID"""
        # Add a member first
        post_response = self.client.post(
            '/members',
            json={"name": "Alice"},
            headers={"Authorization": self.token}
        )
        member_id = post_response.get_json()["id"]

        response = self.client.get(
            f'/members/{member_id}',
            headers={"Authorization": self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], member_id)
        self.assertEqual(response.get_json()["name"], "Alice")

    def test_update_member(self):
        """Test updating a member's name"""
        # Add a member first
        post_response = self.client.post(
            '/members',
            json={"name": "Bob"},
            headers={"Authorization": self.token}
        )
        member_id = post_response.get_json()["id"]

        # Update the member's name
        response = self.client.put(
            f'/members/{member_id}',
            json={"name": "Bob Updated"},
            headers={"Authorization": self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], member_id)
        self.assertEqual(response.get_json()["name"], "Bob Updated")

    def test_delete_member(self):
        """Test deleting a member"""
        # Add a member first
        post_response = self.client.post(
            '/members',
            json={"name": "Charlie"},
            headers={"Authorization": self.token}
        )
        member_id = post_response.get_json()["id"]

        # Delete the member
        response = self.client.delete(
            f'/members/{member_id}',
            headers={"Authorization": self.token}
        )
        self.assertEqual(response.status_code, 204)

        # Verify the member no longer exists
        get_response = self.client.get(
            f'/members/{member_id}',
            headers={"Authorization": self.token}
        )
        self.assertEqual(get_response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
