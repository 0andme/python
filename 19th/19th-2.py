datafile = open('data.txt', 'r')

line = 'init'
while line:
    line = datafile.readline().strip()
    print(line)