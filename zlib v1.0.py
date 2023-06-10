from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://en.my1lib.org/s/%20")
divList = driver.find_elements(By.TAG_NAME, "div")
print(divList)