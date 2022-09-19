from urllib import response
from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_mywatchlist, show_mywatchlist_json, show_mywatchlist_xml, show_mywatchlist_data

# Create your tests here.
class tests(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_show_mywatchlist_url_resolves(self):
        url = reverse('mywatchlist:show_mywatchlist')
        self.assertEquals(resolve(url).func, show_mywatchlist)

    def test_show_mywatchlist_json_url_resolves(self):
        url = reverse('mywatchlist:show_mywatchlist_json')
        self.assertEquals(resolve(url).func, show_mywatchlist_json)

    def test_show_mywatchlist_xml_url_resolves(self):
        url = reverse('mywatchlist:show_mywatchlist_xml')
        self.assertEquals(resolve(url).func, show_mywatchlist_xml)

    # def test_test(self):
    #     response = self.client.get('/show_mywatchlist/xml/', follow=True)
    #     self.assertEquals(response.status_code, 200)