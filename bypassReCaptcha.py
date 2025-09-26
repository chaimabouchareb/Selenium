from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import SessionNotCreatedException
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
"""options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)"""
#universal declaration of the driver
service = Service(executable_path='C:\\webdrivers\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)
options.add_argument("--no-sandbox")
    
driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options = options)
driver.get("https://www.google.com/recaptcha/api2/demo")

driver.maximize_window()
price = driver.find_element_by_xpath("//div[@class='g-recaptcha']")
price_content = price.get_attribute('innerHTML')
start = str(price_content).find(";k=")+len(";k=")
end = str(price_content).find("&amp;co")
driver.implicitly_wait(20)
driver.execute_script("document.getElementById('g-recaptcha-response').style.display = '';")
recaptcha_text_area = driver.find_element_by_id("g-recaptcha-response")
    
recaptcha_text_area.clear()
recaptcha_text_area.send_keys(price_content[start:end])
    #.....................................................................................
    
button = driver.find_element_by_id("recaptcha-demo-submit")