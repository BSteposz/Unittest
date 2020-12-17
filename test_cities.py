import unittest
from city_function import city_country


class FnTest(unittest.TestCase):

    def test_city_country(self):
        fn_city_country = city_country("Paris", "France")
        self.assertEqual(fn_city_country, "Paris France")

    def test_city_country_population(self):
        fn_city_country = city_country('Paris', 'France', '10000')
        self.assertEqual(fn_city_country, "Paris France population: 10000")


if __name__ == '__main__':
    unittest.main()