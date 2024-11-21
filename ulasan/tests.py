from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Ulasan
from penyimpanan.models import Katalog
import json

class UlasanTestCase(TestCase):
   def setUp(self):
       self.user = User.objects.create_user(username='testuser', password='12345')
       self.client = Client()
       self.client.login(username='testuser', password='12345')
       
       self.katalog = Katalog.objects.create(nama='Test Makanan')
       
       self.ulasan = Ulasan.objects.create(
           user=self.user,
           ulasan_makanan_souvenir=self.katalog,
           rating=5,
           pesan_ulasan="Test review"
       )

   def test_show_ulasan(self):
       response = self.client.get(reverse('ulasan:show_ulasan'))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'list_ulasan.html')

   def test_create_ulasan(self):
       response = self.client.post(reverse('ulasan:create_ulasan'), {
           'ulasan_makanan_souvenir': self.katalog.id,
           'rating': 4,
           'pesan_ulasan': 'New test review'
       })
       self.assertEqual(response.status_code, 302) 
       self.assertTrue(Ulasan.objects.filter(pesan_ulasan='New test review').exists())

   def test_add_ulasan_ajax(self):
       response = self.client.post(reverse('ulasan:add_ulasan_ajax'), {
           'ulasan_makanan_souvenir': self.katalog.id,
           'rating': 3,
           'pesan_ulasan': 'Ajax test review'
       })
       self.assertEqual(response.status_code, 201)
       data = json.loads(response.content)
       self.assertEqual(data['pesan_ulasan'], 'Ajax test review')

   def test_edit_ulasan(self):
       response = self.client.post(
           reverse('ulasan:edit_ulasan', args=[self.ulasan.id]), 
           {
               'ulasan_makanan_souvenir': self.katalog.id,
               'rating': 2,
               'pesan_ulasan': 'Edited review'
           }
       )
       self.assertEqual(response.status_code, 302)
       self.ulasan.refresh_from_db()
       self.assertEqual(self.ulasan.pesan_ulasan, 'Edited review')

   def test_delete_ulasan(self):
       response = self.client.get(reverse('ulasan:delete_ulasan', args=[self.ulasan.id]))
       self.assertEqual(response.status_code, 302)
       self.assertFalse(Ulasan.objects.filter(id=self.ulasan.id).exists())

   def test_show_json(self):
       response = self.client.get(reverse('ulasan:show_json'))
       self.assertEqual(response.status_code, 200)
       data = json.loads(response.content)
       self.assertTrue(isinstance(data, list))
       self.assertEqual(len(data), 1)