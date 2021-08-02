from openpyxl import load_workbook
wb = load_workbook('simple_data.xlsx')
data = wb['sheet_test']

area = data['A1:B2']
for row in area:
    for cell in row:
        print(cell.value)

print('-'*20)

cols = data['A:B']
for col in cols:
    for cell in col:
        print(cell.value)

print('-'*20)

rows = data['1:2']
for row in rows:
    for cell in row:
        print(cell.value)
