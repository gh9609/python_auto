from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://container.open.taobao.com/container?appkey=12090519")
driver.find_element(By.XPATH, "//button[@text='授权并登录']").click()

