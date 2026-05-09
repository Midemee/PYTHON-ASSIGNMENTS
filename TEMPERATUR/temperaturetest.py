from unittest import TestCase
import temperature

class TemperatureTest(TestCase):
    def test_that_temperature_is_above_the_threshold(self):
        actual = temperature.temperature_check(100, "C", 30)
        expected = "Heat Alert"
        self.assertEqual(actual, expected)
        
    def test_that_temperature_is_below_the_threshold(self):
        actual = temperature.temperature_check(5, "C", 50)
        expected = "Cold Advisory"
        self.assertEqual(actual, expected)
        
    def test_that_temperature_equal_to_threshold_is_heat_alert(self):
        actual   = temperature.temperature_check(32, "F", 0)
        expected = "Heat Alert"
        self.assertEqual(actual, expected)
        
    def test_invalid_unit_returns_error_message(self):
        actual   = temperature.temperature_check(100, "X", 30)
        expected = "Invalid Input! Unit must be either 'C' or 'F'"
        self.assertEqual(actual, expected)
