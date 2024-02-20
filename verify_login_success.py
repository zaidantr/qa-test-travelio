import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Read credentials from JSON file
with open('credentials.json', 'r') as file:
    creds = json.load(file)

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create WebDriver instance
driver = webdriver.Chrome(options=options)

try:
    URL = 'https://www.travelio.com/'

    driver.get(URL)
    driver.maximize_window()

    # Close modal if present
    try:
        driver.find_element(By.XPATH, "//*[@id='tpmModal']/div/div/div/i").click()
    except:
        pass

    # Click on login button
    login_button = driver.find_element(By.ID, "loginBtn")
    print("'Login button' is visible is:", login_button.is_displayed())
    login_button.click()

    time.sleep(3)

    # Enter login credentials
    email_field = driver.find_element(By.ID, "login-email")
    password_field = driver.find_element(By.ID, "login-password")
    submit_login_button = driver.find_element(By.ID, "login-modal-btn")

    print("Verify email field is visible:", email_field.is_displayed())
    print("Verify password field is visible:", password_field.is_displayed())
    print("Verify submit login button is visible:", submit_login_button.is_displayed())

    email_field.send_keys(creds["email"])
    password_field.send_keys(creds["password"])
    submit_login_button.click()

    time.sleep(3)

    # Verify login success by checking the header name
    header_name = driver.find_element(By.CLASS_NAME, "loggedin-username")
    print("Verify header name 'Zaidan' is:", header_name.text == 'Zaidan')

finally:
    # Close the WebDriver instance
    driver.quit()
    print("Driver is closed")
