user_input = input('Input: ')
datafile = open('textfile.txt', 'w')
datafile.write(user_input+'\n')
datafile.close()