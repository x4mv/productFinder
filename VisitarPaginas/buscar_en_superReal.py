
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import re


def busquedaSuperReal(url, codigoBarras):
    # Abriendo la página SuperMas
    driver = webdriver.Chrome()
    driver.get(url)

    # Enviar los valores del codigo de barra del producto al buscador de superMass 
    producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.amsearch-input")))
    producto.send_keys(codigoBarras)

    # Hacer clic en el botón de búsqueda del buscador de superMass
    buscadorSuperReal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.amsearch-button.-primary.-search.-disabled")))
    driver.execute_script("arguments[0].click();", buscadorSuperReal)

    # Hacer clic en la imagen del producto de superMass
    imagenProductoSuperReal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.product-image-photo.ls-is-cached.lazyloaded")))
    imagenProductoSuperReal.click()

    # Extraer el valor del precio del producto de superMass
    precioReferenciaSuperReal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.price")))
    precioTextoSuperReal = precioReferenciaSuperReal.text.strip()

    # Utilizar una expresión regular para extraer los números del precio actual del producto
    precioFormateadoSuperReal = re.findall(r'\d+\.\d+|\d+', precioTextoSuperReal)

    # Imprimir los números encontrados del precio con descuento
    for precioConDescuentoSuperReal in precioFormateadoSuperReal:
        print("El precio actual en super Real es:", precioConDescuentoSuperReal)

    # Intentar extraer el valor del precio anterior (si los hay) del producto
    try:
        precioSinDescuentoSuperReal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "old-price-15160")))
        precioAntText = precioSinDescuentoSuperReal.text.strip()

        # Utilizar una expresión regular para extraer los números del precio anterior (si los hay) del producto
        precioSinDescuentoFormateadoSuperMas = re.findall(r'\d+\.\d+|\d+', precioAntText)

        # Imprimir los números encontrados del precio anterior (si los hay) del producto
        for precioSinDescuentoSuperReal in precioSinDescuentoFormateadoSuperMas:
            print("El precio sin descuento en super Real es:", precioSinDescuentoSuperReal)
    except:
        precioSinDescuentoSuperReal = "No esta en descuento en superReal"
        print(precioSinDescuentoSuperReal)

        return precioConDescuentoSuperReal, precioSinDescuentoSuperReal

    # Esperar a que se carguen los resultados de búsqueda
    time.sleep(20)  # Puedes ajustar el tiempo de espera según sea necesario