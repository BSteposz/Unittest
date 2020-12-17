from name_function import get_formatted_name

print("Type 'quit' to exit")

while True:
    first = input('\nEnter name ')
    if first == 'quit':
        break
    last = input('Enter surname ')
    if last == 'quit':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tFormatted Name and surname: {formatted_name}")