from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///D:/4th%20semester/webdev/project/login.html")


time.sleep(1)
#absolute Xpath to get username
username_absolute = driver.find_element(By.XPATH, '/html/body/div/fieldset/form/div[1]/input')
#Relative Xpath for password and login_button
password = driver.find_element(By.XPATH, '//*[@id="pwd"]')
login_button = driver.find_element(By.XPATH, '//button[@class="log-in"]')

username_absolute.send_keys("test_user")
password.send_keys("test_pass")
login_button.click()

time.sleep(3)
driver.quit()
