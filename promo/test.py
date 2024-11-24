from django.test import TestCase, Client
from django.utils import timezone

class mainTest(TestCase):
    def test_promo_url_is_exist(self):
        response = Client().get('/promo/')
        self.assertEqual(response.status_code, 200)

    def test_promo_using_main_template(self):
        response = Client().get('/promo/')
        self.assertTemplateUsed(response, 'promo.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)