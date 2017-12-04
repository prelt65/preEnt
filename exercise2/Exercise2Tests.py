import unittest
from models import *
from exercise2 import pomme, orange, addItemsToCart

class Exercise2Tests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def addToCart(self, items):
        self.cart.empty()
        addItemsToCart(self.cart, items.split())

    def test_raises_error_on_invalid_product(self):
        """ Should raise ValueError if the product is not valid """
        with self.assertRaises(ValueError):
            addItemsToCart(self.cart, "pomme orange frites chocolat asd234v.s".split())

    def test_products_total_price(self):
        self.addToCart("pomme pomme orange pomme")
        self.assertEqual(Caisse.calculerTotal(self.cart), 3.05)

        self.addToCart("orange orange orange pomme")
        self.assertEqual(Caisse.calculerTotal(self.cart), 4.35)

        self.addToCart("orange orange orange pomme pomme")
        self.assertEqual(Caisse.calculerTotal(self.cart), 4.95)

    def test_products_simple_offer(self):
        self.addToCart("pomme pomme orange pomme")
        self.assertEqual(Caisse.calculerTotal(self.cart, offre=True), 2.45)

        self.addToCart("orange orange orange pomme")
        self.assertEqual(Caisse.calculerTotal(self.cart, offre=True), 3.1)

        self.addToCart("orange orange orange pomme pomme")
        self.assertEqual(Caisse.calculerTotal(self.cart, offre=True), 3.1)

unittest.main()