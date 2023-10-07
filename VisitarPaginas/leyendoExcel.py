import os
import openpyxl

book = openpyxl.load_workbook(r'C:\Users\IDEAPAD\Desktop\buscador\excel\compras_mensuales_cod_supermas.xlsx')

sheet = book.active

#Codgio del producto

b4 = sheet['B4']

#nombre del producto

c4 = sheet['C4']


print("El codigo del producto es: ",b4.value)

print("El nombre del producto es: ",c4.value)