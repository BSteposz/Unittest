import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        """ Create employee object """
        self.my_employee = Employee('Mariusz', 15000)

    def test_give_default_rise(self):
        """ Test give salary without argument"""

        self.my_employee.give_rise()
        self.assertEqual(self.my_employee.salary, 20000)

    def test_give_custom_rise(self):
        """ Test give salary with argument"""
        self.my_employee.give_rise(15000)
        self.assertEqual(self.my_employee.salary, 30000)




if __name__ == '__main__':
    unittest.main()
