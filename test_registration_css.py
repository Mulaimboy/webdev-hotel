from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///D:/4th%20semester/webdev/project/signup.html")

time.sleep(1)

# Using CSS Selectors to locate elements

# CSS selector for the email input field
email_css = driver.find_element(By.CSS_SELECTOR, 'input[id="email"]')
# CSS selector for the username input field
username_css = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')
# CSS selector for the password input field
password_css = driver.find_element(By.CSS_SELECTOR, 'input[id="pwd"]')
# CSS selector for the confirm password input field
confirm_password_css = driver.find_element(By.CSS_SELECTOR, 'input[id="con-pwd"]')
# CSS selector for the register button
register_button_css = driver.find_element(By.CSS_SELECTOR, 'button.register-btn')

# Fill the signup form using CSS selectors
email_css.send_keys("test_user@example.com")
username_css.send_keys("test_user")
password_css.send_keys("test_password")
confirm_password_css.send_keys("test_password")
register_button_css.click()

time.sleep(3)

driver.quit()
