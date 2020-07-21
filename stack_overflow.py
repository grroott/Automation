from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

#driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

#Stack

driver.get('https://stackoverflow.com/')

driver.maximize_window()

driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()

driver.find_element_by_xpath('//*[@id="email"]').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(os.environ.get('USERNAME'))
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]').click()
driver.find_element_by_xpath('//*[@id="password"]').send_keys(os.environ.get('PASSWORD'))
time.sleep(2)

driver.find_element_by_xpath('//*[@id="submit-button"]').click()
time.sleep(2)

driver.get('https://stackoverflow.com/users/11321166/gokul-nath')

print(driver.find_element_by_xpath('//*[@id="top-cards"]/aside[2]/div/div/div[2]/div[2]/div/div[1]/span').text)
time.sleep(5)

#Insta

driver.get('https://www.instagram.com/')

driver.maximize_window()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(os.environ.get('INSTA_USERNAME'))
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(os.environ.get('INSTA_PASSWORD'))
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
time.sleep(5)

driver.get('https://www.instagram.com/gokulnath_10/')
time.sleep(5)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(result)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

print("Message sent")

time.sleep(5)

driver.close()








