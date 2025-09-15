from app import create_app
import unittest

class TestEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_health_check(self):
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'healthy'})

    def test_identity_validation(self):
        response = self.client.post('/api/validate_identity', json={'id_number': '12345678'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('valid', response.json)

    def test_enrollment(self):
        response = self.client.post('/api/enroll', json={'user_data': {'name': 'John Doe', 'email': 'john@example.com'}})
        self.assertEqual(response.status_code, 201)
        self.assertIn('enrollment_id', response.json)

    def test_document_management(self):
        response = self.client.post('/api/documents', json={'document': 'document_data'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('document_id', response.json)

    def test_digital_contract(self):
        response = self.client.post('/api/contracts', json={'contract_data': 'contract_data'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('contract_id', response.json)

    def test_request_status(self):
        response = self.client.get('/api/request_status/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json)

if __name__ == '__main__':
    unittest.main()