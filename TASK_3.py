from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def login(username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

try:
    # Test Case 1: Valid Login
    login("standard_user", "secret_sauce")
    wait.until(EC.url_contains("inventory"))
    print("Test Case 1 Passed" if "inventory" in driver.current_url else "Test Case 1 Failed")

    # Test Case 2: Invalid Login
    login("wrong_user", "wrong_pass")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    print("Test Case 2 Passed" if "Username and password do not match" in driver.page_source else "Test Case 2 Failed")

    # Test Case 3: Empty Fields
    login("", "")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    print("Test Case 3 Passed" if "Username is required" in driver.page_source else "Test Case 3 Failed")

finally:
    driver.quit()
    print("Browser Closed")
