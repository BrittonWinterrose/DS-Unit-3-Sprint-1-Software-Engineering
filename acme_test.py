#!/usr/bin/env python

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

    def test_default_product_flammability(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_theft_and_stealing(self):
        """Test stealability and explode"""

    def test_default_num_products(self):
        prod = Product('Test Different', price=5, weight=20, flammability=0.7)
        self.assertEqual(prod.flammability, 0.7)
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Keeping those ACME Reports functional!"""
    def test_default_num_products(self):
        """Check if it gets list len 30"""
        test_list = generate_products()
        self.assertEqual(len(test_list), 30, msg="Length is good")

if __name__ == '__main__':
    unittest.main()
