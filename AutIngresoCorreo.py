from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r"/Selenium/chromedriver") #ruta donde esta instalado el driver
driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("tuemail") # ingresas tu correo
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("tupassword")
clave.send_keys(Keys.ENTER)


