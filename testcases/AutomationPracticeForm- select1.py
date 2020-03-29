from selenium import webdriver
import time
from Utilities import xlutils
from Utilities.CustomLogger import Logsetup
from selenium.webdriver.support.ui import Select
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

logger = Logsetup.getlogdemoqa()


Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//a[contains(text(),'Automation practice form')]").click()
time.sleep(5)
select1 = Select(Openchrome.find_element_by_id("continentsmultiple"))
select1.select_by_visible_text("Asia")
select1.select_by_visible_text("Africa")
select1.select_by_visible_text("North America")

select1= Select(Openchrome.find_element_by_id("selenium_commands"))
select1.select_by_visible_text("Wait Commands")