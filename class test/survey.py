
class AnonymousSurvey():

    def __init__(self, question):
        """ Store question and prepare it to taking answere"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Printing question from survey"""
        print(self.question)

    def store_response(self, new_response):
        """Store once answer from a survey question """
        self.responses.append(new_response)
    
    def show_results(self):
        """ Prints all answers """
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")