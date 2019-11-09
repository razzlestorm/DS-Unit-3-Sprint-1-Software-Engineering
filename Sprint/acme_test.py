
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flam(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

# This test isn't working and I'm not sure why. It doesn't fail no matter what
    def test_name_is_str(self):
        """Test that product name is indeed a string."""
        prod = Product(1.0)
        self.assertTrue(isinstance(prod.name, str))


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num_products(self):
        """Test default product quantity being 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test product names are in ADJECTIVES and NOUNS."""
        for prod in generate_products():
            adj, noun = prod.name.split()
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)
# I originally did the above like this, until I looked up assertIn
        '''for prod in generate_products():
            adj, noun = prod.name.split()
            self.assertTrue(adj in ADJECTIVES)
            self.assertTrue(noun in NOUNS)'''

if __name__ == '__main__':
    unittest.main()
