datafile = open('data.csv', 'r')

for line in datafile.readlines():
    data = line.strip().split(',')
    print(data[0])
    print(data[1])
    print(data[2])
    print('-'*10)