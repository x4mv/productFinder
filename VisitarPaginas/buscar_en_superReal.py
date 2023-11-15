
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import re


def busquedaSuperReal(url, codigoBarras, driver):
    # Abriendo la página SuperMas
    
    driver.get(url)

    if codigoBarras == None:
        precioConDescuentoSuperReal = 'NA'
        precioSinDescuentoSuperReal = 'NA'
        descuentoReal = 'NA'
        return precioSinDescuentoSuperReal, precioConDescuentoSuperReal, descuentoReal

    # Enviar los valores del codigo de barra del producto al buscador de superMass 
    producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.amsearch-input")))
    producto.send_keys(codigoBarras)

    # Hacer clic en el botón de búsqueda del buscador de superMass
    buscadorSuperReal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.amsearch-button.-primary.-search.-disabled")))
    driver.execute_script("arguments[0].click();", buscadorSuperReal)

    # Hacer clic en la imagen del producto de superMass
    try:
        imagenProductoSuperReal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.product-image-photo.ls-is-cached.lazyloaded")))
        imagenProductoSuperReal.click()
    except: 
        precioConDescuentoSuperReal = 'NA'
        precioSinDescuentoSuperReal = 'NA'
        descuentoReal = 'NA'
        return precioSinDescuentoSuperReal, precioConDescuentoSuperReal, descuentoReal

    # Extraer el valor del precio del producto de superMass
    precioReferenciaSuperReal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,  '[data-price-type="finalPrice"]')))
    precioTextoSuperReal = precioReferenciaSuperReal.text.strip()

    # Utilizar una expresión regular para extraer los números del precio actual del producto
    precioFormateadoSuperReal = re.findall(r'\d+\.\d+|\d+', precioTextoSuperReal)

    # Imprimir los números encontrados del precio con descuento
    precioConDescuentoSuperReal = precioFormateadoSuperReal[0]
    print("El precio actual en super Real es:", precioConDescuentoSuperReal)

    # Intentar extraer el valor del precio anterior (si los hay) del producto
    try:
        precioSinDescuentoSuperReal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-price-type="oldPrice"]')))
        precioSinDescuentoText = precioSinDescuentoSuperReal.text.strip()

        # Utilizar una expresión regular para extraer los números del precio anterior (si los hay) del producto
        precioSinDescuentoFormateadoSuperMas = re.findall(r'\d+\.\d+|\d+', precioSinDescuentoText)
        precioSinDescuentoSuperReal = precioSinDescuentoFormateadoSuperMas[0]

        descuentoReal = round((100 - (float(precioConDescuentoSuperReal)*100 / float(precioSinDescuentoSuperReal))),2)
        # Imprimir los números encontrados del precio anterior (si los hay) del producto
        print("El precio sin descuento en super Real es: ",precioSinDescuentoSuperReal)
    except:
        precioSinDescuentoSuperReal = "No esta en descuento en superReal"
        print(precioSinDescuentoSuperReal)
        descuentoReal = "NA"

    return precioConDescuentoSuperReal, precioSinDescuentoSuperReal, descuentoReal

