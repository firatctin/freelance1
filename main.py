from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import configparser

#Giriş bilgilerini alıyorum
config = configparser.ConfigParser()
config.read('config.ini')
code = config['dinamik']['kod']
username = config['dinamik']['username']
password = config['dinamik']['password']



driver = webdriver.Chrome()
driver.get('https://bayi.dinamikotomotiv.com.tr/web/login')

WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@name="customer-code"]')))
driver.find_element(by= By.NAME, value = 'customer-code').send_keys(code)
driver.find_element(by = By.NAME, value = 'username').send_keys(username)
driver.find_element(by = By.NAME, value = 'password').send_keys(password)
driver.find_element(by= By.XPATH, value = '/html/body/app-root/app-login/div/div[1]/div[3]/form/div/div/button[2]').click()
WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="uretici"]')))
driver.find_element(by = By.ID, value= 'uretici').click()
brands_list = driver.find_elements(by= By.CSS_SELECTOR, value = '.ng-tns-c135-4.ant-tree-treenode.ng-star-inserted')
time.sleep(20)