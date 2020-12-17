import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """ Test for name_function.py """

    def test_first_last_name(self):

        formatted_name = get_formatted_name('Adam', 'Krawczyk')
        self.assertEqual(formatted_name, 'Adam Krawczyk')



if __name__ == '__main__':
    unittest.main()