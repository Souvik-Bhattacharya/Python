from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\Users\Souvik Bhattacharya\.spyder-py3\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
target = '"Samya"'
string = "!! message using python programming automated web browsing test run!!"
X_arg = '//span[contains(@title,' + target + ')]'
#X_arg = driver.find_element_by_class_name('_3m_Xw')
target = wait.until(EC.presence_of_element_located((By.XPATH,X_arg)))
target.click()
input_box = driver.find_element_by_class_name('p3_M1')
for i in range(100):
    input_box.send_keys(string+Keys.ENTER)