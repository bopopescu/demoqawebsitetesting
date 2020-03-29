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
# Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Selectmenu')]").click()
time.sleep(5)
Openchrome.find_element_by_xpath("//span[@id='speed-button']//span[@class='ui-selectmenu-icon ui-icon ui-icon-triangle-1-s']").click()
time.sleep(5)
# select = Select(Openchrome.find_element_by_xpath("//select[@id='speed']")) # not working because this is not a drop down???
# select.select_by_visible_text("Fast")
Openchrome.find_element_by_xpath("//div[@id='ui-id-1']").click()
# action = ActionChains(Openchrome)
# action.move_to_element(slower).click() # Does not seems to take any action even if it is working

# files menu
#Openchrome.find_element_by_xpath("//span[@id='files-button']//span[@class='ui-selectmenu-icon ui-icon ui-icon-triangle-1-s']").click()
Openchrome.find_element_by_xpath("//span[@id='files-button']").send_keys("Other files")
# time.sleep(5)
# Openchrome.find_element_by_xpath("//li[contains(text(),'Other files')]").click()

# number menu
#Openchrome.find_element_by_xpath("//span[@id='number-button']//span[@class='ui-selectmenu-icon ui-icon ui-icon-triangle-1-s']").click()
#time.sleep(5)
#Openchrome.find_element_by_xpath("//div[@id='ui-id-13']").click()

#select a title menu
# Openchrome.find_element_by_xpath("//span[@id='salutation-button']//span[@class='ui-selectmenu-icon ui-icon ui-icon-triangle-1-s']").click()
# time.sleep(5)
# Openchrome.find_element_by_xpath("//div[@id='ui-id-30").click()

Openchrome.save_screenshot("C:\\Users\Ramya\\PycharmProjects\\demoqa practice\\Screenshots\selectmenu.png")



