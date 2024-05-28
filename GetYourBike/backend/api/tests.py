from django.test import TestCase
from .models import Product, Category

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', category=self.category)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.category.name, 'Test Category')

    def test_product_update(self):
        self.product.name = 'Updated Product'
        self.product.save()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_product_deletion(self):
        product_count_before_delete = Product.objects.count()
        self.product.delete()
        product_count_after_delete = Product.objects.count()
        self.assertEqual(product_count_after_delete, product_count_before_delete - 1)
