from django.test import TestCase
from .models import Product
from category.models import Category

# Create your tests here.
class PercentTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(
            category_name='Catégorie',
            slug='categorie',
            description='Description',
            cat_image='path/image.jpg'
        )

        self.product = Product.objects.create(
            product_name='Jean',
            slug='jean',
            price=20,
            tax_percent=20,
            images='path/image.jpg',
            stock=10,
            category=category
        )
        
    def price_is_valid(self):
        self.assertEqual(self.product.price, 20)
        
    def tax_percent_is_valid(self):
        self.assertEqual(self.product.tax_percent, 20)

    def test_percent_valid(self):
        percent_price = (self.product.price * self.product.tax_percent) / 100
        final_percent_price = self.product.price - percent_price
        self.assertEqual(final_percent_price, 16)

class NoPercentTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(
            category_name='Catégorie',
            slug='categorie',
            description='Description',
            cat_image='path/image.jpg'
        )

        self.product = Product.objects.create(
            product_name='Jean',
            slug='jean',
            price=20,
            tax_percent=0,
            images='path/image.jpg',
            stock=10,
            category=category
        )
        
    def price_is_valid(self):
        self.assertEqual(self.product.price, 20)
        
    def tax_percent_is_valid(self):
        self.assertEqual(self.product.tax_percent, 0)

    def test_percent_valid(self):
        percent_price = (self.product.price * self.product.tax_percent) / 100
        final_percent_price = self.product.price - percent_price
        self.assertEqual(final_percent_price, 20)