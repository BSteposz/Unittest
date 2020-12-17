import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """ Test for name_function.py """

    def test_first_last_name(self):

        formatted_name = get_formatted_name('Adam', 'Krawczyk')
        self.assertEqual(formatted_name, 'Adam Krawczyk')

    def test_first_last_middle_name(self):

        formatted_name = get_formatted_name('Kazimierz', "Tetmajer", 'Przerwa')
        self.assertEqual(formatted_name, 'Kazimierz Przerwa Tetmajer')

if __name__ == '__main__':
    unittest.main()