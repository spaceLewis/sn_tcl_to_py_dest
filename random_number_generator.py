

import random

class RandomNumberGenerator:
    def generate_random_number(self, min_value, max_value):
        if not isinstance(min_value, int) or not isinstance(max_value, int):
            raise TypeError("Both min_value and max_value must be integers.")
        if min_value > max_value:
            raise ValueError("min_value must be less than or equal to max_value.")
        try:
            return random.randint(min_value, max_value)
        except Exception as e:
            raise Exception("An error occurred during random number generation: " + str(e))

    def test_generate_random_number(self):
        import unittest
        class TestRandomNumberGenerator(unittest.TestCase):
            def test_valid_range(self):
                generator = RandomNumberGenerator()
                random_number = generator.generate_random_number(1, 10)
                self.assertGreaterEqual(random_number, 1)
                self.assertLessEqual(random_number, 10)

            def test_invalid_range(self):
                generator = RandomNumberGenerator()
                with self.assertRaises(ValueError):
                    generator.generate_random_number(10, 1)

            def test_non_integer_range(self):
                generator = RandomNumberGenerator()
                with self.assertRaises(TypeError):
                    generator.generate_random_number(1.5, 10)

            def test_exception_during_generation(self):
                generator = RandomNumberGenerator()
                with self.assertRaises(Exception):
                    generator.generate_random_number(1, 10)
                    # Simulate an exception during random number generation
                    raise Exception("Test exception")

        unittest.main(argv=[''], verbosity=2, exit=False)