from selenium import webdriver
import time
from Utilities import xlutils
from Utilities.CustomLogger import Logsetup
from selenium.webdriver.support.ui import Select
import re

logger = Logsetup.getlogdemoqa()


Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Automation practice form')]").click()
time.sleep(5)
Openchrome.find_element_by_name("firstname").send_keys("testnamefirst")
Openchrome.find_element_by_id("lastname").send_keys("testnamelast")
Openchrome.save_screenshot("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\Screenshots\\form1.png")
time.sleep(5)
logger.info("going to hit the submit button and clear the page")
Openchrome.find_element_by_id("submit").click()
time.sleep(5)
Openchrome.find_element_by_name("firstname").send_keys("testnamefirst")
Openchrome.find_element_by_id("lastname").send_keys("testnamelast")
Openchrome.find_element_by_id("sex-0").click()
Openchrome.find_element_by_id("exp-2").click()
Openchrome.find_element_by_id("datepicker").send_keys("12/25/2020")
Openchrome.find_element_by_id("profession-0").click()
Openchrome.find_element_by_id("profession-1").click()
Openchrome.find_element_by_id("tool-0").click()
Openchrome.find_element_by_id("tool-1").click()
Openchrome.find_element_by_id("tool-2").click()
continent =Openchrome.find_element_by_id("continents").send_keys("Australia")
# select = Select(continent)
# select.select_by_visble_text("Australia")
textoutput = Openchrome.find_element_by_tag_name("Body").text
print (textoutput)
print(type(textoutput))
storelist  = list(re.split('" "|\n',textoutput))
print (storelist)