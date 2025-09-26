from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\webdrivers\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(10)
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

time.sleep(30)

driver.quit()
