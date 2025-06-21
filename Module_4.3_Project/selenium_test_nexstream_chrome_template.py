#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:22:14 2024

@author: anthonymauro
copywrite NexStream Technical Education, LLC
All rights reserved
"""

##**************************************************************##
# FIRST NEED TO DOWNLOAD CHROMEDRIVER AND SAVE 
# INTO YOUR MACHINE DRIVER SEARCH PATH 
# (e.g. /usr/local/bin)
##**************************************************************##

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#Create a Selenium logger instance, set the level to log DEBUG msgs
#and add file handle for stderr
logger = None
logger.None
handler = None
logger.addHandler(handler)


# Instantiate options
#options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(None)

#From home page, go to teacher training page 
#   (home --> training button)
time.sleep(5)
teachers = driver.find_element(by=By.CLASS_NAME, value ='menu-item-24').click()
wait = WebDriverWait(driver, timeout=5)

try:
   assert wait.until(lambda d : driver.find_element(by=By.LINK_TEXT, value ='Training Programs').is_displayed())
except:
   print("Timeout error on Training Programs page navigation")

teacher_training = driver.find_element(by=By.LINK_TEXT, value ='Training Programs').click()


#Fill out request for more info form and submit it
#NOTE - not all fields are filled out in this template

#Locate the name box and enter text
more_info_name = driver.find_element(None)
more_info_name.send_keys("YOUR TEXT ENTRY)

#Locate the message box and enter text
more_info_number = driver.find_element(None)
more_info_name.send_keys("YOUR TEXT ENTRY)

#Locate the submit button and enter text
submit = driver.find_element(None)
submit.click()


#Do the confirmation in the exception below
#Check if the thank you message was issued
try:
    #assert driver.find_element(by=By.XPATH, value="//div[text()='Thank you for your message. It has been sent.']")
   assert wait.until(lambda d : driver.find_element(by=By.XPATH, value="//div[text()='Thank you for your message. It has been sent.']").is_displayed())
except:
   try:
      assert wait.until(lambda d : driver.find_element(by=By.XPATH, value="//div[text()='One or more fields have an error. Please check and try again.']").is_displayed())
      print("****** ERROR:  Request email was not sent - Not all fields were filled out *******")
   except:
      print("****** ERROR:  Request email was not sent - Something went wrong...Likely a timeout error, check wait timeout value!  *******")
else:
   print('TEST SUCCESS - MORE INFO REQUEST FROM TRAINING PAGE VIA CHROME - MESSAGE SENT')
      
        
time.sleep(2)
driver.close()
driver.quit()