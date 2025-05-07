from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# === CONFIG ===
TEST_FILE_PATH = "file:///D:/4th%20semester/webdev/project/payment.html"

# === SETUP ===
def setup_driver():
    driver = webdriver.Chrome()
    driver.get(TEST_FILE_PATH)
    time.sleep(1)
    return driver

# === FILL FORM FUNCTION ===
def fill_form(driver, data):
    driver.find_element(By.ID, "name").send_keys(data["name"])
    driver.find_element(By.ID, "email").send_keys(data["email"])
    driver.find_element(By.ID, "address").send_keys(data["address"])
    driver.find_element(By.ID, "country").send_keys(data["country"])
    driver.find_element(By.ID, "State").send_keys(data["state"])
    driver.find_element(By.ID, "code").send_keys(data["postal"])
    driver.find_element(By.ID, "cardholder").send_keys(data["cardholder"])
    driver.find_element(By.ID, "card-number").send_keys(data["card_number"])
    driver.find_element(By.ID, "cvc").send_keys(data["cvc"])
    driver.find_element(By.ID, "month").send_keys(data["month"])
    driver.find_element(By.ID, "year").send_keys(data["year"])
    time.sleep(0.5)
    driver.find_element(By.TAG_NAME, "form").submit()

# === TEST CASES ===
test_cases = [
    {
        "name": "Empty Form",
        "data": {
            "name": "",
            "email": "",
            "address": "",
            "country": "",
            "state": "",
            "code": "",
            "cardholder": "",
            "card_number": "",
            "cvc": "",
            "month": "",
            "year": ""
        }
    },
    {
        "name": "Invalid Email Format",
        "data": {
            "name": "Alice",
            "email": "alice-at-example.com",
            "address": "10 Street",
            "country": "USA",
            "state": "TX",
            "code": "73301",
            "cardholder": "Alice",
            "card_number": "4111111111111111",
            "cvc": "123",
            "month": "01",
            "year": "2026"
        }
    },
    {
        "name": "Invalid Card Number (Too Short)",
        "data": {
            "name": "Bob",
            "email": "bob@example.com",
            "address": "22 Main Blvd",
            "country": "USA",
            "state": "NV",
            "code": "88901",
            "cardholder": "Bob",
            "card_number": "12345678",
            "cvc": "321",
            "month": "06",
            "year": "2027"
        }
    },
    {
        "name": "Invalid CVC (Too Long)",
        "data": {
            "name": "Charlie",
            "email": "charlie@example.com",
            "address": "789 Palm Ave",
            "country": "USA",
            "state": "FL",
            "code": "33101",
            "cardholder": "Charlie",
            "card_number": "4111111111111111",
            "cvc": "12345",
            "month": "07",
            "year": "2024"
        }
    },
    {
        "name": "Expired Card Year",
        "data": {
            "name": "Diana",
            "email": "diana@example.com",
            "address": "55 Old Rd",
            "country": "USA",
            "state": "WA",
            "code": "98001",
            "cardholder": "Diana",
            "card_number": "4111111111111111",
            "cvc": "789",
            "month": "09",
            "year": "2021"
        }
    },
    {
        "name": "Invalid Zip Code (Letters)",
        "data": {
            "name": "Evan",
            "email": "evan@example.com",
            "address": "100 Block St",
            "country": "USA",
            "state": "OR",
            "code": "ABCDE",
            "cardholder": "Evan",
            "card_number": "4111111111111111",
            "cvc": "234",
            "month": "04",
            "year": "2026"
        }
    },
    {
        "name": "Cardholder Name with Numbers",
        "data": {
            "name": "Frank",
            "email": "frank@example.com",
            "address": "200 Hill Rd",
            "country": "USA",
            "state": "AZ",
            "code": "85001",
            "cardholder": "Frank123",
            "card_number": "4111111111111111",
            "cvc": "456",
            "month": "10",
            "year": "2026"
        }
    },
    {
        "name": "Special Characters in Name",
        "data": {
            "name": "@#%$!",
            "email": "strange@example.com",
            "address": "404 Mystery Ln",
            "country": "USA",
            "state": "NM",
            "code": "87501",
            "cardholder": "@#%$!",
            "card_number": "4111111111111111",
            "cvc": "999",
            "month": "03",
            "year": "2027"
        }
    },
    {
        "name": "Valid Non-USA Address",
        "data": {
            "name": "George",
            "email": "george@example.co.uk",
            "address": "221B Baker St",
            "country": "UK",
            "state": "London",
            "code": "NW16XE",
            "cardholder": "George",
            "card_number": "4111111111111111",
            "cvc": "321",
            "month": "12",
            "year": "2027"
        }
    },
    {
        "name": "Future Year and Month",
        "data": {
            "name": "Helen",
            "email": "helen@example.com",
            "address": "789 High Tower",
            "country": "USA",
            "state": "CO",
            "code": "80014",
            "cardholder": "Helen",
            "card_number": "4111111111111111",
            "cvc": "888",
            "month": "08",
            "year": "2035"
        }
    },
    {
        "name": "Valid Data",
        "data": {
            "name": "John Doe",
            "email": "john@example.com",
            "address": "123 Main Street",
            "country": "USA",
            "state": "CA",
            "postal": "12345",
            "cardholder": "John Doe",
            "card_number": "4111111111111111",
            "cvc": "123",
            "month": "08",
            "year": "2026"
        }
    },
    {
        "name": "Invalid Email",
        "data": {
            "name": "Jane Smith",
            "email": "janesmith.com",  # invalid
            "address": "Street 12",
            "country": "UK",
            "state": "London",
            "postal": "AB123",
            "cardholder": "Jane Smith",
            "card_number": "4111111111111111",
            "cvc": "123",
            "month": "12",
            "year": "2026"
        }
    },
    {
        "name": "Short Card Number",
        "data": {
            "name": "Tester",
            "email": "test@example.com",
            "address": "Tester Address",
            "country": "Testland",
            "state": "TS",
            "postal": "00000",
            "cardholder": "Test Card",
            "card_number": "123456",  # invalid
            "cvc": "123",
            "month": "05",
            "year": "2026"
        }
    },
    {
        "name": "Expired Year",
        "data": {
            "name": "Old User",
            "email": "old@example.com",
            "address": "Old Street",
            "country": "Nowhere",
            "state": "OldState",
            "postal": "99999",
            "cardholder": "Old User",
            "card_number": "4111111111111111",
            "cvc": "123",
            "month": "05",
            "year": "2022"  # invalid
        }
    },
    
]

# === RUN TESTS ===
for case in test_cases:
    print(f"\nRunning Test Case: {case['name']}")
    
    try:
        driver = setup_driver()
        fill_form(driver, case["data"])
        time.sleep(2)

        # Basic success detection (you can customize this depending on your actual behavior)
        # E.g., a success message, redirection, alert, etc.
        if "Thank you" in driver.page_source or "Success" in driver.page_source:
            print(f"[PASS] {case['name']} succeeded as expected.")
        else:
            print(f"[WARN] {case['name']} completed, but no success message detected. Check behavior manually.")
    except Exception as e:
        print(f"[FAIL] {case['name']} failed due to error: {e}")
    finally:
        driver.quit()

