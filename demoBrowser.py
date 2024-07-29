import time
from selenium import webdriver


driver = webdriver.Edge()
time.sleep(2)
driver.get("https://rahulshettyacademy.com")
time.sleep(2)
driver.maximize_window()
print(driver.title)
print(driver.current_url)