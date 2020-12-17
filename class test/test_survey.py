import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ Test for AnonymousSurvey class """

    def setUp(self):
        question = "Favourite book"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Słownik języka polskiego', 'recepty', 'Manuale']
        

    def test_store_single_response(self):
        """ Check single answer is correctly taken """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    
    def test_store_multi_response(self):
        """ Check multi answer is correctly taken """

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)



if __name__ == '__main__':
    unittest.main()