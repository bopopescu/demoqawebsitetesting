from selenium import webdriver
import time
from Utilities import xlutils
from Utilities.CustomLogger import Logsetup
from selenium.webdriver.support.ui import Select
import re
import os.path
from os.path import exists

logger = Logsetup.getlogdemoqa()


Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//li[6]//a[1]").click()
time.sleep(5)
Openchrome.find_element_by_id("browseFile").send_keys("C:\\Python\\mahesh.jpg")
time.sleep(5)
Openchrome.find_element_by_xpath("//button[@id='uploadButton']").click()
alert = Openchrome.switch_to_alert()
msg = alert.text
print(msg)
alert.accept()

