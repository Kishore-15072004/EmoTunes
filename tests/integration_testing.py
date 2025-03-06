import unittest
from app import app
import json

class TestAppIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_recommend(self):
        with open('tests/test_image_base64.txt', 'r') as file:
            image_base64 = file.read()
        result = self.app.post('/recommend',
                               data=json.dumps({'image': image_base64}),
                               content_type='application/json')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.get_data())
        self.assertIn('emotion', data)
        self.assertIn('weather', data)
        self.assertIn('playlists', data)

if __name__ == '__main__':
    unittest.main()
