from openpyxl import Workbook
from openpyxl.styles import Font
from leyendoExcel import b4, c4
from buscar_en_superMas import busquedaSuperMas
from buscar_en_superReal import busquedaSuperReal
from datetime import datetime
import leyendoExcel


#Desempaquetar los resultados de la funcion superMas
preciosSuperMas = busquedaSuperMas("https://www.supermas.com.py/",7896110011158)
precioConDescuentoSuperMas, precioSinDescuentoSuperMas, descuento = preciosSuperMas

#Desempaquetar los resultados de la funcion SuperReal
preciosSuperReal = busquedaSuperReal("https://www.realonline.com.py/",7798303170713)
precioConDescuentoSuperReal, precioSinDescuentoSuperReal = preciosSuperReal


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

sheet['C1'] = 'Descuento al por mayor Supermass'
sheet['C1'].font = Font(bold=True)
sheet['C2'] = f"A partir de {descuento[0]} es GS {descuento[1]}"


sheet['D1'] = 'Precio sin Descuento Supermass '
sheet['D1'].font = Font(bold=True)
sheet['D2'] = precioSinDescuentoSuperMas


sheet['E1'] = 'Precio con Descuento superMass'
sheet['E1'].font = Font(bold=True)
sheet['E2'] = precioConDescuentoSuperMas

sheet['F1'] = 'Descuento en super Real (%)'
sheet['F1'].font = Font(bold=True)
sheet['F2'] = round(100 - (float(precioConDescuentoSuperReal)*100 / float(precioSinDescuentoSuperReal)),2)


sheet['G1'] = 'Precio con Descuento Real'
sheet['G1'].font = Font(bold=True)
sheet['G2'] = precioConDescuentoSuperReal


sheet['H1'] = 'Precio sin Descuento Real'
sheet['H1'].font = Font(bold=True)
sheet['H2'] = precioSinDescuentoSuperReal

# Extraer la fecha de la consulta
fecha = datetime.now().strftime("%m_%d_%y")


# Guardar el libro de trabajo
book.save(f"Productos_Supermercados_prueba_{fecha}.xlsx")
