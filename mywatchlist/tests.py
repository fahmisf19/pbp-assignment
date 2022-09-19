from urllib import response
from django.test import Client, TestCase

# Create your tests here.
class tests(TestCase):

    def test_url(self):
        response = self.client.get('/mywatchlist/', follow=True)
        self.assertEqual(response.status_code, 200)
        
    def test_url_xml(self):
        response = self.client.get('/mywatchlist/xml/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        response = self.client.get('/mywatchlist/json/', follow=True)
        self.assertEqual(response.status_code, 200)
    