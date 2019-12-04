from django.tests import SimpleTestCase, Client
from django.urls import reverse, resolve
from Pages.views import *

class Test_Pages_Urls(SimpleTestCase):
    def test_app_global(self):
        url = reverse('')
        self.assertEquals(resolve(url).func, app_admin_view)