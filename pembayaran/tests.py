from django.test import TestCase, Client
from django.urls import reverse
from .models import Pembayaran
from penyimpanan.models import Katalog
from django.contrib.messages import get_messages

class PembayaranViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.katalog_item = Katalog.objects.create(nama="Product 1", harga=10000)
        self.payment = Pembayaran.objects.create(
            product=self.katalog_item,
            status='Success',
            payment_method='bank_transfer',
            amount=2,
            total_payment=20000
        )

    def test_create_payment_view_get(self):
        response = self.client.get(reverse('pembayaran:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pembayaran/create_payment.html')

    def test_create_payment_view_post(self):
        data = {
            'product': self.katalog_item.id,
            'amount': 1,
            'payment_method': 'bank_transfer',
            'total_payment': 10000
        }
        response = self.client.post(reverse('pembayaran:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Pembayaran.objects.filter(amount=1, total_payment=10000).exists())

    def test_create_payment_view_post_invalid(self):
        # Test POST request to create_payment with invalid data
        data = {
            'product': self.katalog_item.id,
            'amount': '',  # Invalid data
            'payment_method': 'bank_transfer',
            'total_payment': 10000
        }
        response = self.client.post(reverse('pembayaran:create'), data)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Mohon perbaiki kesalahan berikut.')

    def test_payment_history_view(self):
        # Test payment_history view
        response = self.client.get(reverse('pembayaran:payment_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pembayaran/payment_history.html')
        self.assertContains(response, 'Product 1')

    def test_update_payment_view_get(self):
        # Test GET request to update_payment
        response = self.client.get(reverse('pembayaran:update_payment', args=[self.payment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pembayaran/update_payment.html')

    def test_update_payment_view_post(self):
        # Test POST request to update_payment with valid data
        data = {
            'product': self.katalog_item.id,
            'amount': 3,
            'payment_method': 'credit_card',
            'total_payment': 30000
        }
        response = self.client.post(reverse('pembayaran:update_payment', args=[self.payment.id]), data)
        self.assertEqual(response.status_code, 302)
        updated_payment = Pembayaran.objects.get(id=self.payment.id)
        self.assertEqual(updated_payment.amount, 3)
        self.assertEqual(updated_payment.total_payment, 30000)

    def test_delete_payment_view(self):
       
        response = self.client.post(reverse('pembayaran:delete_payment', args=[self.payment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Pembayaran.objects.filter(id=self.payment.id).exists())
