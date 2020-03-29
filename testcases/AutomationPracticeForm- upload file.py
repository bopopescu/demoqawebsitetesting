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
Openchrome.find_element_by_xpath("//a[contains(text(),'Automation practice form')]").click()
time.sleep(5)
Openchrome.find_element_by_id("photo").send_keys("C:\\Python\\mahesh.jpg")