from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Ulasan
from penyimpanan.models import Katalog

class UlasanTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.katalog_item = Katalog.objects.create(nama='Sample Makanan')
        self.client.login(username='testuser', password='12345')

    def test_create_ulasan(self):
        response = self.client.post(reverse('ulasan:create_ulasan'), {
            'ulasan_makanan_souvenir': self.katalog_item.pk,
            'rating': 5,
            'pesan_ulasan': 'Test review'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Ulasan.objects.count(), 1)  

    def test_show_ulasan(self):
        Ulasan.objects.create(user=self.user, ulasan_makanan_souvenir=self.katalog_item, rating=4, pesan_ulasan="Review content")
        response = self.client.get(reverse('ulasan:show_ulasan'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Review content')

    def test_delete_ulasan(self):
        ulasan = Ulasan.objects.create(user=self.user, ulasan_makanan_souvenir=self.katalog_item, rating=4, pesan_ulasan="To be deleted")
        response = self.client.post(reverse('ulasan:delete_ulasan', args=[ulasan.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ulasan.objects.count(), 0)  

    def test_show_json(self):
        Ulasan.objects.create(user=self.user, ulasan_makanan_souvenir=self.katalog_item, rating=4, pesan_ulasan="JSON review")
        response = self.client.get(reverse('ulasan:show_json'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  

    def test_add_ulasan_ajax(self):
        response = self.client.post(reverse('ulasan:add_ulasan_ajax'), {
            'nama_makanan_souvenir': self.katalog_item.pk,
            'rating': 5,
            'pesan_ulasan': 'AJAX review'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Ulasan.objects.count(), 1)
        self.assertEqual(Ulasan.objects.first().pesan_ulasan, 'AJAX review')
