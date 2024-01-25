import unittest
import main


class Test_calculate_area_of_rectangle(unittest.TestCase):

    def test_expected_result_integer(self):
        result = main.calculate_area_of_rectangle(5, 5)
        self.assertEqual(result, 25)

    def test_expected_result_float(self):
        result = main.calculate_area_of_rectangle(3.55, 3.55)
        self.assertEqual(result, 12.6025)

    def test_negative_number_ValueError(self):
        with self.assertRaises(ValueError):
            main.calculate_area_of_rectangle(1, -1)

    def test_zero_number_ValueError(self):
        with self.assertRaises(ValueError):
            main.calculate_area_of_rectangle(1, 0)

    def test_zero_and_negative_number_ValueError(self):
        with self.assertRaises(ValueError):
            main.calculate_area_of_rectangle(-1, 0)

    def test_string_input_TypeError(self):
        with self.assertRaises(TypeError):
            main.calculate_area_of_rectangle('a', 5)

    def test_expected_result_Boolean_True(self):
        result = main.calculate_area_of_rectangle(True, 5.0)
        self.assertEqual(result, 5.0)

    def test_Boolean_ValueError(self):
        with self.assertRaises(ValueError):
            main.calculate_area_of_rectangle(False, 5.0)

    def test_input_strings_throws_TypeError(self):
        # You cannot multiply two strings
        with self.assertRaises(TypeError):
            main.calculate_area_of_rectangle('a', 'b')

    def test_input_string_float_TypeError(self):
        # You cannot multiply a float and a string
        with self.assertRaises(TypeError):
            main.calculate_area_of_rectangle('a', 5.0)


if __name__ == '__main__':
    unittest.main()
