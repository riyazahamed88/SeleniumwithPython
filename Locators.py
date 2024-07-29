import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,"input[name='name").send_keys("rahul")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(2)
driver.find_element(By.ID,"inlineRadio1").click()
# xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# Css - tagname[attribute ='value'] -> //input[@type ='submit'] , #id ,.classname
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "success" in message
driver.find_element(By.XPATH,"(//input[@type='text']) [3]").send_keys("helloagain")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text']) [3]").clear()
