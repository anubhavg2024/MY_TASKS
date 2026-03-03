from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "username"
ACCESS_KEY = "access_key"

BROWSER = "Chrome"

bstack_options = {
    "os": "Windows",
    "osVersion": "10",
    "projectName": "Cross Browser Testing",
    "buildName": "Build 1",
    "sessionName": f"OrangeHRM Login Test - {BROWSER}"
}

if BROWSER == "Chrome":
    options = webdriver.ChromeOptions()
elif BROWSER == "Firefox":
    options = webdriver.FirefoxOptions()
elif BROWSER == "Edge":
    options = webdriver.EdgeOptions()
else:
    raise Exception("Unsupported Browser!")

options.set_capability("browserName", BROWSER)
options.set_capability("browserVersion", "latest")
options.set_capability("bstack:options", bstack_options)

# Connect to BrowserStack
driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    options=options
)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.visibility_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    wait.until(EC.url_contains("dashboard"))
    print(f"✅ Login Successful on {BROWSER}")

except Exception as e:
    print(f"❌ Test Failed on {BROWSER}:", e)

finally:
    driver.quit()
