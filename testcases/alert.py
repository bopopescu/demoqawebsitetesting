from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//aside[2]//ul[1]//li[1]//a[1]").click()
Openchrome.find_element_by_xpath("//button[@id='alert']").click()
time.sleep(5)
alert = Openchrome.switch_to_alert()
alerttext = alert.text
alert.accept()
print (alerttext)

# alert_obj.accept() – used to accept the Alert
# alert_obj.dismiss() – used to cancel the Alert
# alert.send_keys() – used to enter a value in the Alert text box
# alert.text() – used to retrieve the message included in the Alert pop-up



