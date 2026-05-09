from unittest import TestCase
import promocode

class TestPromoCode(TestCase):
    def test_that_promo_save10_apply_discount(self):
        actual = promocode.apply_discount("Mango", 100, "SAVE10")
        expected = 90.0
        self.assertEqual(actual,expected)
        
    def test_that_promo_halfoff_apply_discount(self):
        actual = promocode.apply_discount("Juice", 300, "HALFOFF")
        expected = 150.0
        self.assertEqual(actual, expected)
        
    def test_that_invalid_promocode_apply_no_discount(self):
        actual = promocode.apply_discount("Apple", 500, "INVALIDCODE")
        expected = 500.0
        self.assertEqual(actual, expected)

    def test_that_invalid_promocode_apply_no_discount(self):
        actual = promocode.apply_discount("Apple", 500, "")
        expected = 500.0
        self.assertEqual(actual, expected)
        
        
