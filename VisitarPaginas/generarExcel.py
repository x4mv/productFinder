from openpyxl import Workbook
from openpyxl.styles import Font
from leyendoExcel import b4, c4
from buscar_en_superMas import busquedaSuperMas
from buscar_en_superReal import busquedaSuperReal
from datetime import datetime
from leyendoExcel import arrayCodigos, arrayNombreProducto

# Crear un libro de trabajo
book = Workbook()
sheet = book.active

# Escribir el encabezado
sheet['A1'] = 'Código de barras'
sheet['A1'].font = Font(bold=True)
sheet['B1'] = 'Nombre del producto'
sheet['B1'].font = Font(bold=True)
sheet['C1'] = 'Descuento al por mayor Supermass'
sheet['C1'].font = Font(bold=True)
sheet['D1'] = 'Precio sin Descuento Supermass '
sheet['D1'].font = Font(bold=True)
sheet['E1'] = 'Precio Actual superMass'
sheet['E1'].font = Font(bold=True)
sheet['F1'] = 'Descuento en super Real (%)'
sheet['F1'].font = Font(bold=True)
sheet['G1'] = 'Precio Actual Real'
sheet['G1'].font = Font(bold=True)
sheet['H1'] = 'Precio sin Descuento Real'
sheet['H1'].font = Font(bold=True)
# Extraer la fecha de la consulta
fecha = datetime.now().strftime("%m_%d_%y")

#automatizar para todos los productos
counter = 2   
for codigoProducto in range(len(arrayCodigos)):
    
    #Desempaquetar los resultados de la funcion superMas
    print("El nombre del producto es: ", arrayNombreProducto[codigoProducto])
    preciosSuperMas = busquedaSuperMas("https://www.supermas.com.py/", arrayCodigos[codigoProducto])
    precioConDescuentoSuperMas, precioSinDescuentoSuperMas, descuento = preciosSuperMas

    #Desempaquetar los resultados de la funcion SuperReal
    preciosSuperReal = busquedaSuperReal("https://www.realonline.com.py/",arrayCodigos[codigoProducto])
    precioConDescuentoSuperReal, precioSinDescuentoSuperReal, descuentoReal = preciosSuperReal

    sheet[f'A{counter}'] = arrayCodigos[codigoProducto]
    sheet[f'B{counter}'] = arrayNombreProducto[codigoProducto]
    sheet[f'C{counter}'] = f"A partir de {descuento[0]} es GS {descuento[1]}"
    sheet[f'D{counter}'] = precioSinDescuentoSuperMas
    sheet[f'E{counter}'] = precioConDescuentoSuperMas
    sheet[f'F{counter}'] = descuentoReal
    sheet[f'G{counter}'] = precioConDescuentoSuperReal
    sheet[f'H{counter}'] = precioSinDescuentoSuperReal

    counter = counter + 1
    





# Guardar el libro de trabajo
book.save(f"Productos_Supermercados_prueba_{fecha}.xlsx")



