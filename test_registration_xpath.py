from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///D:/4th%20semester/webdev/project/signup.html")

time.sleep(1)

# Absolute XPaths for the input fields and buttons
# Absolute XPath to get email input
email_absolute = driver.find_element(By.XPATH, '/html/body/div/fieldset/form/div[1]/input')
# Absolute XPath to get username input
username_absolute = driver.find_element(By.XPATH, '/html/body/div/fieldset/form/div[2]/input')
# Absolute XPath to get password input
password_absolute = driver.find_element(By.XPATH, '/html/body/div/fieldset/form/div[3]/input')
# Absolute XPath to get confirm password input
confirm_password_absolute = driver.find_element(By.XPATH, '/html/body/div/fieldset/form/div[4]/input')
# Absolute XPath to get the register button
register_button_absolute = driver.find_element(By.XPATH, '/html/body/div/fieldset/form/button')

# Relative XPaths for the input fields and buttons
# Relative XPath for email input
email_relative = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
# Relative XPath for username input
username_relative = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
# Relative XPath for password input
password_relative = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
# Relative XPath for confirm password input
confirm_password_relative = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
# Relative XPath for the register button
register_button_relative = driver.find_element(By.XPATH, '//button[@class="register-btn"]')

# Fill the signup form using absolute paths
email_absolute.send_keys("test_user@example.com")
username_absolute.send_keys("test_user")
password_absolute.send_keys("test_password")
confirm_password_absolute.send_keys("test_password")
register_button_absolute.click()

time.sleep(3)

# Fill the signup form using relative paths (just for comparison)
email_relative.send_keys("test_user@example.com")
username_relative.send_keys("test_user")
password_relative.send_keys("test_password")
confirm_password_relative.send_keys("test_password")
register_button_relative.click()

time.sleep(3)

driver.quit()
