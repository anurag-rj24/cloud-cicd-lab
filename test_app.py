import unittest
from app import app, AUTHOR_NAME, VERSION

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint_status(self):
        """Test that /health returns HTTP 200"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_health_endpoint_payload(self):
        """Test that /health returns correct JSON data"""
        response = self.app.get('/health')
        data = response.get_json()
        self.assertEqual(data.get('status'), 'healthy')
        self.assertEqual(data.get('version'), VERSION)
        self.assertEqual(data.get('author'), AUTHOR_NAME)

    def test_index_page_status(self):
        """Test that / returns HTTP 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_content(self):
        """Test that / contains developer name and pipeline info"""
        response = self.app.get('/')
        self.assertIn(AUTHOR_NAME.encode(), response.data)
        self.assertIn(b"Kubernetes", response.data)

if __name__ == '__main__':
    unittest.main()
