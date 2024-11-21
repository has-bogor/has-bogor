from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from penyimpanan.models import Katalog
from .models import Wishlist

class WishlistTestCase(TestCase):
    def setUp(self):
        # Set up a test user and product
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Tambahkan harga saat membuat instance Katalog
        self.product1 = Katalog.objects.create(nama='Product 1', deskripsi='Description for product 1', harga=10000)
        self.product2 = Katalog.objects.create(nama='Product 2', deskripsi='Description for product 2', harga=20000)

    def test_add_to_wishlist(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        # Add product to wishlist
        response = self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product1.id]))
        self.assertEqual(response.status_code, 302)  # Expect redirect after adding

        # Check if product is in wishlist
        self.assertTrue(Wishlist.objects.filter(user=self.user, product=self.product1).exists())

    def test_wishlist_view(self):
        # Log in the user and add a product to the wishlist
        self.client.login(username='testuser', password='password')
        Wishlist.objects.create(user=self.user, product=self.product1)

        # Access wishlist view
        response = self.client.get(reverse('wishlist:wishlist_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')

    def test_update_wishlist(self):
        # Log in the user and add product1 to the wishlist
        self.client.login(username='testuser', password='password')
        wishlist_item = Wishlist.objects.create(user=self.user, product=self.product1)

        # Update wishlist item to product2
        response = self.client.post(reverse('wishlist:update_wishlist', args=[self.product1.id]), {
            'new_product_id': self.product2.id
        })
        self.assertEqual(response.status_code, 302)  # Expect redirect after updating
        wishlist_item.refresh_from_db()
        self.assertEqual(wishlist_item.product, self.product2)

    def test_remove_from_wishlist(self):
        # Log in the user and add product to the wishlist
        self.client.login(username='testuser', password='password')
        Wishlist.objects.create(user=self.user, product=self.product1)

        # Remove product from wishlist
        response = self.client.post(reverse('wishlist:remove_from_wishlist', args=[self.product1.id]))
        self.assertEqual(response.status_code, 302)  # Expect redirect after removing

        # Check if product is removed from wishlist
        self.assertFalse(Wishlist.objects.filter(user=self.user, product=self.product1).exists())
