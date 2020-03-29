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

Openchrome.find_element_by_xpath("//a[contains(text(),'Automation practice form')]").click()
time.sleep(5)
Openchrome.find_element_by_id("continents")
continent =Openchrome.find_element_by_id("continents")
select = Select(continent)
select.select_by_visible_text("South America")
Openchrome.save_screenshot("C:\\Users\Ramya\\PycharmProjects\\demoqa practice\\Screenshots\dropdown1.png")
time.sleep(3)
select.select_by_visible_text("Australia")
Openchrome.save_screenshot("C:\\Users\Ramya\\PycharmProjects\\demoqa practice\\Screenshots\dropdown2.png")

# Method1 ------- with ActionChains-----------------

action = ActionChains(Openchrome)
Asia = Openchrome.find_element_by_xpath("//*[@id='continentsmultiple']/option[1]")
NorthAmerica = Openchrome.find_element_by_xpath("//*[@id='continentsmultiple']/option[6]")
Africa = Openchrome.find_element_by_xpath("//*[@id='continentsmultiple']/option[3]")
ActionChains(Openchrome).key_down(Keys.CONTROL).click(Asia).key_up(Keys.CONTROL).perform()
ActionChains(Openchrome).key_down(Keys.CONTROL).click(Africa).key_up(Keys.CONTROL).perform()
ActionChains(Openchrome).key_down(Keys.CONTROL).click(NorthAmerica).key_up(Keys.CONTROL).perform()
Openchrome.save_screenshot("C:\\Users\Ramya\\PycharmProjects\\demoqa practice\\Screenshots\mutipleselect.png")


