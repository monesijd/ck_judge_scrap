from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import random


def scrap():
    driver = webdriver.Chrome()
    driver.get('https://ckj.imslab.org/#/signin')
    time.sleep(3)
    username = driver.find_element(By.ID, "input-74")
    username.send_keys(os.environ['account'])

    username = driver.find_element(By.ID, "input-78")

    username.send_keys(os.environ['password'])
    button = driver.find_element(By.XPATH, "//button[contains(@class, 'primary-button') and @type='button' and contains(., 'Sign in')]")
    button.click()

    time.sleep(3)

    pageSource = driver.page_source
    mycount = pageSource.count("New bonus")
    driver.close()
    return mycount


pre = 0
while(1):
    time.sleep(random.uniform(0, 1))
    now = scrap()
    if(pre != now):
        print("有新的 CK judge 加分作業")
        pre = now
    else:
        print("not change")
