import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://google.com")
driver.implicitly_wait(10)
inp_elm = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
inp_elm.click()
ActionChains(driver).send_keys('cuaca hari ini').perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()

file = driver.save_screenshot('cuaca.png')
time.sleep(1000)
