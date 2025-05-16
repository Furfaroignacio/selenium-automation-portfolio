from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import os

def iniciar_driver():
    return webdriver.Chrome()

def login(driver, usuario, contrasena):
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    campo_usuario = wait.until(
        EC.presence_of_element_located((By.ID, "username")))
    campo_usuario.send_keys(usuario)
    campo_contrasena = wait.until(
        EC.presence_of_element_located((By.ID, "password")))
    campo_contrasena.send_keys(contrasena)
    boton = driver.find_element(By.CLASS_NAME, "radius")
    boton.click()

def verificar_resultado(driver):
    try: 
        mensaje = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text
        if "You logged into a secure area!" in mensaje:
            print("✅ Login exitoso")
            driver.save_screenshot("capturas/login_exitoso.png")
        elif "Your username is invalid!" in mensaje or "Your password is invalid!" in mensaje:
            print("❌ Login fallido")
            driver.save_screenshot("capturas/login_fallido.png")
        else:
            print("⚠️ Resultado inesperado")
    except:
        print("❌ No se pudo verificar el login")

def main():
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    driver = iniciar_driver()
    login(driver, usuario, contrasena)
    verificar_resultado(driver)
    driver.quit()

if __name__ == "__main__":
    main()


