from django.test import TestCase, Client
from django.urls import reverse
from .models import Promo
import json
import uuid
from django.contrib.auth.models import User

class PromoViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.promo = Promo.objects.create(
            id=uuid.uuid4(),
            kode="PROMO123",
            potongan=10,
            masa_berlaku="30",
            minimal_transaksi=100000,
            toko_terkait=[]
        )
        # Login as superuser or any necessary setup for user authentication
        self.user = User.objects.create_superuser(username='admin', password='password')
        self.client.login(username='admin', password='password')

    def test_show_promo_admin(self):
        response = self.client.get(reverse('promo:show_promo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promo.html')

    def test_create_promo(self):
        data = {
            'kode': 'NEWPROMO',
            'potongan': 15,
            'masa_berlaku': '60',
            'minimal_transaksi': 50000,
            'toko_terkait': json.dumps([])
        }
        response = self.client.post(reverse('promo:create_promo'), data)
        self.assertEqual(response.status_code, 302)  # Expect redirect
        self.assertTrue(Promo.objects.filter(kode='NEWPROMO').exists())

    def test_edit_promo(self):
        data = {
            'kode': 'UPDATEDPROMO',
            'potongan': 20,
            'masa_berlaku': '90',
            'minimal_transaksi': 75000,
            'toko_terkait': json.dumps([])
        }
        response = self.client.post(reverse('promo:edit_promo', args=[self.promo.id]), data)
        self.promo.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.promo.kode, 'UPDATEDPROMO')

    def test_delete_promo(self):
        response = self.client.post(reverse('promo:delete_promo', args=[self.promo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Promo.objects.filter(id=self.promo.id).exists())

    def test_add_related_store(self):
        new_store = {'name': 'Store A'}
        response = self.client.post(
            reverse('promo:add_store', args=[self.promo.id]),
            data=json.dumps(new_store),
            content_type="application/json"
        )
        self.promo.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertIn(new_store, self.promo.toko_terkait)

    def test_remove_related_store(self):
        self.promo.toko_terkait = [{'name': 'Store A'}]
        self.promo.save()
        remove_store_data = {'storeName': 'Store A'}
        response = self.client.post(
            reverse('promo:remove_store', args=[self.promo.id]),
            data=json.dumps(remove_store_data),
            content_type="application/json"
        )
        self.promo.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertNotIn({'name': 'Store A'}, self.promo.toko_terkait)

    def test_show_filtered_promo(self):
        response = self.client.get(reverse('promo:show_filtered_promo') + '?sort_by=potongan')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertGreaterEqual(data[0]['fields']['potongan'], data[-1]['fields']['potongan'])

