import openpyxl

book = openpyxl.load_workbook('compras_mensuales_cod_supermas.xlsx')
sheet = book.active

b3 = sheet['B3']
b4 = sheet['B4']

print(b3.value)
print(b4.value)