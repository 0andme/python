from openpyxl import load_workbook
wb = load_workbook('simple_data.xlsx')
data = wb.active

row = data['2']
for cell in row:
    print(cell.value)

print('-'*20)

col = data['A']
for cell in col:
    print(cell.value)