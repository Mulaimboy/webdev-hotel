from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/4th%20semester/webdev/project/login.html")
time.sleep(1) 

username = driver.find_element(By.CSS_SELECTOR, "#username")      # ID selector
password = driver.find_element(By.CSS_SELECTOR, "#pwd")           # ID selector
login_button = driver.find_element(By.CSS_SELECTOR, "button.log-in")  # class selector for button

# Interact with the form
username.send_keys("test_css")
password.send_keys("test_cssselector")
login_button.click()

time.sleep(3)
driver.quit()
