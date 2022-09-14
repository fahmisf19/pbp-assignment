from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

# Create your tests here.
class tests(SimpleTestCase):

    def test_show_katalog_url_resolves(self):
        url = reverse('katalog:show_katalog')
        self.assertEquals(resolve(url).func, show_katalog)