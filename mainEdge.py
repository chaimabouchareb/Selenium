from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service(executable_path='C:\\webdrivers\\msedgedriver.exe')
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
driver.get("https://cevasanteanimale-tstv11.outsystemsenterprise.com/PHP/")
time.sleep(10)
driver.find_element(By.CLASS_NAME, "submenu OSInline is--dropdown").click()

time.sleep(50)

driver.quit()
