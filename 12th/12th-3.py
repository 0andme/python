def print_filter(string):
    if 'skip' in string:
        print('Skip')
        return
    
    print(string)

user_input = ''
while user_input != 'quit':
    user_input = input('Input: ')
    print_filter(user_input)