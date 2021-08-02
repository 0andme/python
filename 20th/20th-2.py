values = []
values.append(('alghost', 'fastone'))
values.append(('yskim', 'fastcampus'))
values.append(('jelee', 'fastfive'))

datafile = open('result.csv', 'w')

for line in values:
    data = ','.join(line)
    datafile.write(data+'\n')
datafile.close()