from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")  
wait = WebDriverWait(driver, 10)

username = wait.until(EC.visibility_of_element_located((By.ID, "username")))

username.send_keys("tomsmith")

# PASSWORD

password = wait.until(EC.visibility_of_element_located((By.ID, "password")))

password.send_keys("SuperSecretPassword!")

# LOGIN BUTTON

login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "radius")))

login_button.click()

driver.save_screenshot("login_success.png")

print("Login successful")

input("Press Enter to close...")