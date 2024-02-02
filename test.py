from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
driver = webdriver.Chrome()

website = 'http://localhost:5173'

# testing the login page
driver.get('/'.join([website, 'login']))
driver.maximize_window()

username = "yahiaa05"
password = "AdminAdmin123@"
driver.find_element(by=By.XPATH, value='//*[@id="name"]').send_keys(username)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/div/div/button').click()

# testing the signup page


username = "mohamed"
password = "12345678"
email = 'ab@gmail.com'


time.sleep(5)
driver.quit()