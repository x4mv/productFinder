from openpyxl import Workbook
from openpyxl.styles import Font
from leyendoExcel import b4, c4
from main import precioAntValor, precioValor

import time

# Crear un libro de trabajo
book = Workbook()
sheet = book.active

# Escribir el encabezado
sheet['A1'] = 'Código de barras'
sheet['A1'].font = Font(bold=True)

sheet['A2'] = b4.value

sheet['B1'] = 'Nombre del producto'
sheet['B1'].font = Font(bold=True)

sheet['B2'] = c4.value

sheet['C1'] = 'Precio Original superMass'
sheet['C1'].font = Font(bold=True)

sheet['C2'] = precioAntValor

sheet['D1'] = 'Precio Descuento superMass'
sheet['D1'].font = Font(bold=True)

sheet['D2'] = precioValor

sheet['E1'] = 'Porcentaje Descuento superMass'
sheet['E1'].font = Font(bold=True)

sheet['F1'] = 'Precio Original Real'
sheet['F1'].font = Font(bold=True)

sheet['G1'] = 'Precio Descuento Real'
sheet['G1'].font = Font(bold=True)

sheet['H1'] = 'Porcentaje Descuento Real'
sheet['H1'].font = Font(bold=True)

# Extraer la fecha de la consulta
fecha = time.strftime('%x')
sheet['I1'] = 'Fecha De consulta'
sheet['I1'].font = Font(bold=True)
sheet['I2'] = fecha

# Guardar el libro de trabajo
book.save('prueba1.xlsx')
