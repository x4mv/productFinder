
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import re


def busquedaSuperMas(url, codigoBarras):

    if codigoBarras == None:
        precioConDescuentoSuperMas = 'NA'
        precioSinDescuentoSuperMas = 'NA'
        descuento = ['NA', 'NA']
        return precioSinDescuentoSuperMas, precioConDescuentoSuperMas, descuento
    # Abriendo la página SuperMas
    driver = webdriver.Chrome()
    driver.get(url)

    # Enviar los valores del codigo de barra del producto al buscador de superMass 
    producto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search")))
    producto.send_keys(codigoBarras)

    # Hacer clic en el botón de búsqueda del buscador de superMass
    buscadorSuperMas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    buscadorSuperMas.click()

    # Hacer clic en la imagen del producto de superMass
    try:
        imagenProductoSuperMas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.wp-post-image.lazy.loaded")))
        imagenProductoSuperMas.click()
    except:
        precioConDescuentoSuperMas = 'NA'
        precioSinDescuentoSuperMas = 'NA'
        descuento = ['NA', 'NA']
        return precioSinDescuentoSuperMas, precioConDescuentoSuperMas, descuento


    #Extraerel descuento aplicable en superMas
    try:
        cantidadDescuentoSuperMas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.financiacion")))
        descuentoSinFormateo = cantidadDescuentoSuperMas.text
        descuento = re.findall(r'\d+\.\d+|\d+', descuentoSinFormateo)
        print(f"El descuento aplicable en superMas es: A partir de {descuento[0]} unidades es GS {descuento[1]}")
    except: 
        descuento = "no hay descuento"



    # Extraer el valor del precio del producto de superMass
    precioReferenciaSuperMas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "producto-precio")))
    precioTextoSuperMas = precioReferenciaSuperMas.text.strip()

    # Utilizar una expresión regular para extraer los números del precio actual del producto
    precioFormateadoSuperMas = re.findall(r'\d+\.\d+|\d+', precioTextoSuperMas)


    # Imprimir los números encontrados del precio con descuento
    for precioConDescuentoSuperMas in precioFormateadoSuperMas:
        print("El precio actual en SuperMas es:", precioConDescuentoSuperMas)

    # Intentar extraer el valor del precio anterior (si los hay) del producto
    try:
        precioSinDescuentoSuperMas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "producto-precio-anterior")))
        precioAntText = precioSinDescuentoSuperMas.text.strip()

        # Utilizar una expresión regular para extraer los números del precio anterior (si los hay) del producto
        precioSinDescuentoFormateadoSuperMas = re.findall(r'\d+\.\d+|\d+', precioAntText)

        # Imprimir los números encontrados del precio anterior (si los hay) del producto
        for precioSinDescuentoSuperMas in precioSinDescuentoFormateadoSuperMas:
            print("El precio sin descuento en SuperMas es:", precioSinDescuentoSuperMas)
    except:
        precioSinDescuentoSuperMas = "No esta en descuento en SuperMas"
        print(precioSinDescuentoSuperMas)

    

    return precioConDescuentoSuperMas, precioSinDescuentoSuperMas, descuento
