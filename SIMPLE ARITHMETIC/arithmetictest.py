from unittest import TestCase
import arithmetic

class ArithmeticTest(TestCase):

    def test_that_check_answer_returns_true_for_correct_answer(self):
        actual = arithmetic.check_answer(10, 4, 6)
        expected = True
        self.assertEqual(actual, expected)

    def test_that_check_answer_returns_false_for_wrong_answer(self):
        actual = arithmetic.check_answer(10, 4, 5)
        expected = False
        self.assertEqual(actual, expected)

    def test_that_calculate_score_returns_correct_percentage(self):
        actual = arithmetic.calculate_score(7, 10)
        expected = 70.0
        self.assertEqual(actual, expected)

    def test_that_calculate_score_returns_100_for_perfect_score(self):
        actual = arithmetic.calculate_score(10, 10)
        expected = 100.0
        self.assertEqual(actual, expected)

    def test_that_calculate_score_returns_0_for_no_correct_answers(self):
        actual = arithmetic.calculate_score(0, 10)
        expected = 0.0
        self.assertEqual(actual, expected)
