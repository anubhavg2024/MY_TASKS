from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 30)

try:
    print("Opening SauceDemo site...")
    driver.get("https://www.saucedemo.com")

    # Login
    print("Logging in...")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add item
    print("Adding product to cart...")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    # Go to cart
    print("Navigating to cart...")
    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    # Checkout
    print("Proceeding to checkout...")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout"))
    ).click()

    # ✅ WAIT for checkout form to load properly
    print("Filling checkout information...")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "first-name"))
    ).send_keys("Anubhav")

    driver.find_element(By.ID, "last-name").send_keys("Goswami")
    driver.find_element(By.ID, "postal-code").send_keys("700001")
    driver.find_element(By.ID, "continue").click()

    # Finish
    print("Completing purchase...")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "finish"))
    ).click()

    # Verify
    success_message = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header"))
    ).text

    if "Thank you for your order!" in success_message:
        print("✅ Checkout Successful!")
    else:
        print("❌ Checkout Failed!")

finally:
    driver.quit()
    print("Test Completed Successfully.")
