from selenium import webdriver
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from datetime import date

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
# Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Checkboxradio')]").click()
time.sleep(3)
newyorkradiobutton ="//label[contains(text(),'New York')]"
parisradiobutton = "//label[contains(text(),'Paris')]"
londonradiobutton = "//label[contains(text(),'London')]"
twostarradiobutton = "//label[contains(text(),'2 Star')]"
threestarradiobutton = "//label[contains(text(),'3 Star')]"
fourstarradiobutton = "//label[contains(text(),'4 Star')]"
fivestarradiobutton = "//label[contains(text(),'5 Star')]"
twodoubleradiobutton = "//label[contains(text(),'2 Double')]"
twoqueenradiobutton = "//label[contains(text(),'2 Queen')]"
onequeenradiobutton = "//label[contains(text(),'1 Queen')]"
onekingradiobutton = "//label[contains(text(),'1 King')]"

Openchrome.find_element_by_xpath(newyorkradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(parisradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(londonradiobutton).click()

Openchrome.find_element_by_xpath(twostarradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(threestarradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(fourstarradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(fivestarradiobutton).click()

Openchrome.find_element_by_xpath(twodoubleradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(twoqueenradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(onekingradiobutton).click()
time.sleep(3)
Openchrome.find_element_by_xpath(onequeenradiobutton).click()

