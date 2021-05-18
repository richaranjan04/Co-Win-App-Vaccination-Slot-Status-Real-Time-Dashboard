# Python version 3.8 , pip3

import selenium       
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path of webdriver on personal system
path = '/Users/richaranjan/Downloads/chromedriver'

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://www.cowin.gov.in/home")
time.sleep(5)

pin_area = driver.find_element_by_id('mat-input-0')

pin = input('Enter pincode for finding nearest vaccination centers :')
print(pin)
pin_area.send_keys(pin)  # Enter the pincode of your own area

driver.find_element_by_xpath('//button[normalize-space()="Search"]').click()

target = driver.find_element_by_class_name('carousel-inner')
driver.execute_script('arguments[0].scrollIntoView(true);', target)

driver.find_element_by_xpath("//label[contains(text(), 'Age 18+')]").click()

# Loop as many times as you want to refresh the page [0-infinity]. For demo perpose i have taken 5.
i=0
while (i<5 ):
    driver.find_element_by_xpath('//button[normalize-space()="Search"]').click()
    driver.find_element_by_xpath("//label[contains(text(), 'Age 18+')]").click()
    time.sleep(30) # Refresh page after ever 30 sec. Can be increaded/decreased accordingly.
    i=i+1

driver.quit()
driver.close()







