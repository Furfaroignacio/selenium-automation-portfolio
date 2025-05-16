from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.csvWritter import guardaCsv


def iniciarDriver():
    return webdriver.Chrome()

# abrimos el link mercadolibre buscamoes un producto que llega como parametro y clikc enter
def buscarProducto(driver, busqueda):
    driver.get("https://www.mercadolibre.com.ar/")
    
    wait = WebDriverWait(driver, 10)
    caja_busqueda = wait.until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )
    caja_busqueda.send_keys(busqueda)
    caja_busqueda.send_keys(Keys.RETURN)
    

def extraerDatos(driver, cantidad=10):
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.ui-search-layout__item"))
    )    
    productos = driver.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")
    datos = []
    for prod in productos[:10]:
        try:
            nombre = prod.find_element(By.CLASS_NAME, "poly-component__title").text
            precio = prod.find_element(By.CLASS_NAME, "poly-price__current").text
            datos.append({
                'Nombre': nombre,
                'Precio': precio
        })
        except:
            continue
    return datos



def main():
    busqueda = input("¿Qué producto deseas buscar? ")
    driver = iniciarDriver()
    buscarProducto(driver, busqueda)
    datos = extraerDatos(driver)
    guardaCsv(datos, archivo=f"{busqueda}_resultados.csv")
    driver.quit()

if __name__ == "__main__":
    main()

