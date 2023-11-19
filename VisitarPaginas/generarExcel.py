from openpyxl import Workbook
from openpyxl.styles import Font
from buscar_en_superMas import busquedaSuperMas
from buscar_en_superReal import busquedaSuperReal
from datetime import datetime
from leyendoExcel import arrayCodigos, arrayNombreProducto
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import getpass
import os

# Instancia del navegador fuera del bucle
driver = webdriver.Chrome()



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
sheet['F1'] = 'Precio Actual Real'
sheet['F1'].font = Font(bold=True)
sheet['G1'] = 'Precio sin Descuento Real'
sheet['G1'].font = Font(bold=True)


#automatizar para todos los productos

counter = 2   
for codigoProducto in range(len(arrayCodigos)):
    
    try: 
        #Desempaquetar los resultados de la funcion superMas
        
        preciosSuperMas = busquedaSuperMas("https://www.supermas.com.py/", arrayCodigos[codigoProducto], driver)
        precioConDescuentoSuperMas, precioSinDescuentoSuperMas, descuento = preciosSuperMas

        sheet[f'A{counter}'] = arrayCodigos[codigoProducto]
        sheet[f'B{counter}'] = arrayNombreProducto[codigoProducto]
        sheet[f'C{counter}'] = f"A partir de {descuento[0]} es GS {descuento[1]}"
        sheet[f'D{counter}'] = precioSinDescuentoSuperMas
        sheet[f'E{counter}'] = precioConDescuentoSuperMas
        counter = counter + 1
        precioConDescuentoSuperMas = ""
        precioSinDescuentoSuperMas = ""
        descuento = ["", ""]

    except TimeoutException as e:
        print(f"Error de tiempo de espera en la primera página: {e}")







counter2 = 2
for codigoProducto2 in range(len(arrayCodigos)):
    
    try:
    #Desempaquetar los resultados de la funcion SuperReal
        preciosSuperReal = busquedaSuperReal("https://www.realonline.com.py/",arrayCodigos[codigoProducto2], driver)
        precioConDescuentoSuperReal, precioSinDescuentoSuperReal = preciosSuperReal
        sheet[f'F{counter2}'] = precioConDescuentoSuperReal
        sheet[f'G{counter2}'] = precioSinDescuentoSuperReal
        counter2 = counter2 + 1
        precioConDescuentoSuperReal = ""
        precioSinDescuentoSuperReal = ""

    except TimeoutException as e:
        print(f"Error de tiempo de espera en la segunda página: {e}")
        
    




driver.quit()

# Guardar el libro de trabajo
# Extraer la fecha de la consulta
fecha = datetime.now().strftime("%m_%d_%y")


#obtener el usuario
user = getpass.getuser()
current_directory = os.getcwd()

# Obtener la ruta del escritorio
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Construir la ruta del archivo usando el escritorio y el nombre del archiv
file_name = f'Productos_Supermercados_prueba_{fecha}.xlsx'
file_path = os.path.join(desktop_path, file_name)


book.save(file_path)




