
class Employee(object):
    """ Random class to exercise Unittest """

    def __init__(self, name, yearly_salary):

        self.name = name
        self.salary = yearly_salary

    def give_rise(self, rise=5000):
        self.salary += rise

