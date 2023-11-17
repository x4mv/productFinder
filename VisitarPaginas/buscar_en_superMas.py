
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re


def busquedaSuperMas(url, codigoBarras,driver):

    if codigoBarras == None:
        precioConDescuentoSuperMas = '-'
        precioSinDescuentoSuperMas = '-'
        descuento = ['-', '-']
        return precioSinDescuentoSuperMas, precioConDescuentoSuperMas, descuento
    # Abriendo la página SuperMas
    driver.get(url)

    # Enviar los valores del codigo de barra del producto al buscador de superMass 
    producto = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search")))
    producto.send_keys(codigoBarras)

    # Hacer clic en el botón de búsqueda del buscador de superMass
    buscadorSuperMas = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    buscadorSuperMas.click()

    # Hacer clic en la imagen del producto de superMass
    try:
        imagenProductoSuperMas = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.wp-post-image.lazy.loaded")))
        imagenProductoSuperMas.click()
    except:
        precioConDescuentoSuperMas = '-'
        precioSinDescuentoSuperMas = '-'
        descuento = ['-', '-']
        return precioSinDescuentoSuperMas, precioConDescuentoSuperMas, descuento


    #Extraerel descuento aplicable en superMas
    try:
        cantidadDescuentoSuperMas = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.financiacion")))
        descuentoSinFormateo = cantidadDescuentoSuperMas.text
        descuento = re.findall(r'\d+\.\d+|\d+', descuentoSinFormateo)
        
    except: 
        descuento = ["-", "-"]

    # Extraer el valor del precio del producto de superMass
    precioReferenciaSuperMas = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "producto-precio")))
    precioTextoSuperMas = precioReferenciaSuperMas.text.strip()

    # Utilizar una expresión regular para extraer los números del precio actual del producto
    precioFormateadoSuperMas = re.findall(r'\d+\.\d+|\d+', precioTextoSuperMas)

    precioConDescuentoSuperMas = precioFormateadoSuperMas[0]

    # Intentar extraer el valor del precio anterior (si los hay) del producto
    try:
        precioSinDescuentoSuperMas = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "producto-precio-anterior")))
        precioAntText = precioSinDescuentoSuperMas.text.strip()

        # Utilizar una expresión regular para extraer los números del precio anterior (si los hay) del producto
        precioSinDescuentoFormateadoSuperMas = re.findall(r'\d+\.\d+|\d+', precioAntText)
        
        
        precioSinDescuentoSuperMas = precioSinDescuentoFormateadoSuperMas[0]
        return precioConDescuentoSuperMas, precioSinDescuentoSuperMas, descuento

    except:
        precioSinDescuentoSuperMas = "-"
        

        
        return precioConDescuentoSuperMas, precioSinDescuentoSuperMas, descuento
    