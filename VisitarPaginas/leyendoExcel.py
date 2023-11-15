import os
import openpyxl

book = openpyxl.load_workbook(r'C:\Users\IDEAPAD\Desktop\buscador\excel\compras_mensuales_cod_supermas.xlsx')

sheet = book.active

#Codigo del producto

b4 = sheet['B4']

#nombre del producto
#sheet.max_row
c4 = sheet['C4']

#Arreglo con los codigos 
arrayCodigos = []

#Arreglo con los Nombres 
arrayNombreProducto = []

# Itera a través de todas las filas en la hoja de trabajo
for filaCodigo in sheet.iter_rows(min_row=4, max_row = sheet.max_row, min_col =2, max_col = 3, values_only=True):
    # `fila` es una tupla que contiene los valores de cada celda en la fila actual
    if filaCodigo[0] != None:
        arrayCodigos.append(filaCodigo[0])
        arrayNombreProducto.append(filaCodigo[1])

# print("Los codigos de los productos son: ", arrayCodigos)
print("Los Nombres de los productos son: ", arrayNombreProducto)

