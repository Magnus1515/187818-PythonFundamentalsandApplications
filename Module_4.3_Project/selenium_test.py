import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a logger instance
logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('sel_debug.log')
logger.addHandler(handler)

driver = webdriver.Firefox();

driver.get("https://magento.softwaretestingboard.com/")
# driver.implicitly_wait(0.5)
driver.maximize_window()

# now is working with the menu item 
button = driver.find_element(By.ID, "ui-id-3")
button.click()
# <a href="/computers">Computers </a>

link = driver.find_element(By.LINK_TEXT, "Create an Account")
link.click()

first_name = driver.find_element(By.ID, "firstname")
# time.sleep(2)
first_name.send_keys("Michael")

last_name = driver.find_element(By.ID, "lastname")
#time.sleep(2)
last_name.send_keys("Jordan")

email = driver.find_element(By.ID, "email_address")
#time.sleep(2)
email.send_keys("michael.jordan10@gmail.com")

password = driver.find_element(By.ID, "password")
#time.sleep(2)
password.send_keys("Michael12345")

password_confirmation = driver.find_element(By.ID, "password-confirmation")
#time.sleep(2)
password_confirmation.send_keys("Michael12345")

createAccount_button = link = driver.find_element(By.CLASS_NAME, "primary")
createAccount_button.click()


try: 
  confirmation_message = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, "//*[text()='Thank you for registering with Main Website Store.']"))
  )

  print("✅ TEST SUCCESFULL:", confirmation_message.text)

except: 
  print("❌ THERE WAS AN ERROR IN THE PROCESS")

driver.close()
driver.quit()
