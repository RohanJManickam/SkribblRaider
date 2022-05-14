import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os

PATH = os.getcwd() + '\chromedriver.exe'
driver = webdriver.Chrome(PATH)

loopCount = 0

while True:
    driver.get("https://skribbl.io")
    print("connected to skribbl")

    time.sleep(5)

    user = driver.find_element_by_xpath('//*[@id="inputName"]')

    user.send_keys("Tom Bartlet  ")
    user.send_keys(Keys.RETURN)

    time.sleep(5)

    field = driver.find_element_by_xpath('//*[@id="inputChat"]')


    while(True):
        try: 
            field.send_keys("*SPAM GOES HERE")
        except:
            break
        else:
            field.send_keys(Keys.RETURN)
            time.sleep(random.uniform(0.75, 1.5))

    loopCount += 1
    print('Script has run', loopCount, 'times')