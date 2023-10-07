#openpyxl 

from openpyxl import Workbook
from openpyxl.styles import Font
import time

book = Workbook()
sheet = book.active


#escribiendo el encabezado

sheet['A1'] = 'codigo de barras'
sheet['A1'].font = Font(bold = True)

sheet['B1'] = 'Nombre del producto'
sheet['B1'].font = Font(bold = True)

sheet['C1'] = 'Precio Original superMass'
sheet['C1'].font = Font(bold = True)

sheet['D1'] = 'Precio Descuento superMass'
sheet['D1'].font = Font(bold = True)

sheet['E1'] = 'Porcentaje Descuento superMass'
sheet['E1'].font = Font(bold = True)

sheet['F1'] = 'Precio Original Real'
sheet['F1'].font = Font(bold = True)

sheet['G1'] = 'Precio Descuento Real'
sheet['G1'].font = Font(bold = True)

sheet['H1'] = 'Porcentaje Descuento Real'
sheet['H1'].font = Font(bold = True)

#extraer la fecha de la consulta

fecha = time.strftime('%x')
sheet['H1'] = 'Fecha De consulta'
sheet['H1'].font = Font(bold = True)
sheet['H2'] = fecha





book.save('prueba_escritura_1.xlsx')