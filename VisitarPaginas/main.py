import leyendoExcel
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
producto.send_keys(leyendoExcel.b4.value)

# Hacer clic en el botón de búsqueda
buscador = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
buscador.click()

# Hacer clic en la imagen del producto 
imagenProducto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.wp-post-image.lazy.loaded")))
imagenProducto.click()

# Extraer el valor del precio del producto
precioRef = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "producto-precio")))
precioText = precioRef.text.strip()

# Utilizar una expresión regular para extraer los números del precio actual del producto
precioFormat = re.findall(r'\d+\.\d+|\d+', precioText)

# Imprimir los números encontrados del precio actual del producto
for precioValor in precioFormat:
    print("El precio actual es:", precioValor)

# Intentar extraer el valor del precio anterior (si los hay) del producto
try:
    precioAntRef = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "producto-precio-anterior")))
    precioAntText = precioAntRef.text.strip()

    # Utilizar una expresión regular para extraer los números del precio anterior (si los hay) del producto
    precioAntFormat = re.findall(r'\d+\.\d+|\d+', precioAntText)

    # Imprimir los números encontrados del precio anterior (si los hay) del producto
    for precioAntValor in precioAntFormat:
        print("El precio anterior es:", precioAntValor)
except:
    print("NA")

# Esperar a que se carguen los resultados de búsqueda
time.sleep(30)  # Puedes ajustar el tiempo de espera según sea necesario

