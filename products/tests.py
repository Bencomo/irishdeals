from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    define the tests
    run vs post models - testing products in the terminal
    """
    
    def test_str(self):
        test_name = Product(name='product')
        self. assertEqual(str(test_name), 'product')
