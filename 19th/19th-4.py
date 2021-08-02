user_input = input('Input: ')
datafile = open('textfile.txt', 'a')
datafile.write(user_input+'\n')
datafile.close()