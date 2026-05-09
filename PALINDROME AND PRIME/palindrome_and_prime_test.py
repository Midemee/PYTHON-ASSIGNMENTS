from unittest import TestCase
from palindrome_and_prime import *


class TestPalindrome(TestCase):

    def test_that_the_palindrome_is_correct(self):
        self.assertEqual(palindrome(787), "Number is a palindrome")
        
    def test_that_the_palindrome_is_incorrect(self):
        self.assertEqual(palindrome(783), "Number is not a palindrome")
              
    def test_that_the_prime_number_is_correct(self):
        self.assertEqual(prime(7), "Number is a prime number")
      
    def test_that_the_prime_number_is_incorrect(self):
        self.assertEqual(prime(8), "Number is not a prime number")
