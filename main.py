from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import re

# Abriendo la página SuperMas
driver = webdriver.Chrome()
driver.get("https://www.supermas.com.py/")

# Buscar producto 
producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search")))
producto.send_keys("7797453000659")

# Hacer clic en el botón de búsqueda
buscador = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
buscador.click()

# Hacer clic en la imagen del producto 
imagenProducto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.wp-post-image.lazy.loaded")))
imagenProducto.click()

# Extraer el valor del precio del producto
precioProductoReferencia = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "producto-precio")))
precioProductoValor = precioProductoReferencia.text.strip()

# Utilizar una expresión regular para extraer los números del precio actual del producto
numeros_encontrados_precio_actual = re.findall(r'\d+\.\d+|\d+', precioProductoValor)

# Imprimir los números encontrados del precio actual del producto
for numero_actual in numeros_encontrados_precio_actual:
    print("El precio actual es:", numero_actual)

# Intentar extraer el valor del precio anterior (si los hay) del producto
try:
    precioAnteriorProductoReferencia = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "producto-precio-anterior")))
    precioAnteriorProductoValor = precioAnteriorProductoReferencia.text.strip()

    # Utilizar una expresión regular para extraer los números del precio anterior (si los hay) del producto
    numeros_encontrados_precio_anterior = re.findall(r'\d+\.\d+|\d+', precioAnteriorProductoValor)

    # Imprimir los números encontrados del precio anterior (si los hay) del producto
    for numero_anterior in numeros_encontrados_precio_anterior:
        print("El precio anterior es:", numero_anterior)
except:
    print("No se encontró un precio anterior.")

# Esperar a que se carguen los resultados de búsqueda
time.sleep(60)  # Puedes ajustar el tiempo de espera según sea necesario

# Cerrar el navegador
driver.quit()
