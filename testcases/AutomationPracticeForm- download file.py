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
Openchrome.find_element_by_xpath("//a[contains(text(),'Selenium Automation Hybrid Framework')]").click()
Openchrome.find_element_by_xpath("//a[contains(text(),'Test File to Download')]").click()
time.sleep(15)

if os.path.exists("C:\\Users\\Mahesh\\Downloads\\OnlineStore.zip") == True:
    print ("test zip file exist - download sucessful")
else:
    print ("file not found")

if os.path.exists("C:\\Users\\Mahesh\\Downloads\\Test-File-to-Download.xlsx") == True:
    print ("test excel file exist - download sucessful")
else:
    print ("file not found")