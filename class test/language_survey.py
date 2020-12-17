from survey import AnonymousSurvey

# Define question and make survey

question = 'Favourite book'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'quit' to exit\n")

while True:
    response = input("Book: ")
    if response == 'quit':
        break
    my_survey.store_response(response)

print("\nThanks for answer")
my_survey.show_results()