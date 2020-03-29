from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from datetime import date

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Controlgroup')]").click()
time.sleep(3)

cartype = "//select[@id='car-type']"
standardradiobutton = "//*[@id='content']/div[2]/div/fieldset[1]/div/label[1]/span[1]"
automaticradiobutton = "//*[@id='content']/div[2]/div/fieldset[1]/div/label[2]/span[1]"
insurancecheckbox = "//*[@id='content']/div[2]/div/fieldset[1]/div/label[3]/span[1]"
noofcarinputbox="//input[@id='horizontal-spinner']"
spinnerup = "//*[@id='content']/div[2]/div/fieldset[1]/div/span[2]/a[1]/span[1]"
spinnerdown ="//*[@id='content']/div[2]/div/fieldset[1]/div/span[2]/a[2]/span[1]"
booknow="//*[@id='content']/div[2]/div/fieldset[1]/div/button"

vcartype = "//span[@id='ui-id-8-button']"
vstandardradiobutton = "//*[@id='content']/div[2]/div/fieldset[2]/div/label[1]"
vautomaticradiobutton = "//*[@id='content']/div[2]/div/fieldset[2]/div/label[2]"
vinsurancecheckbox = "//*[@id='content']/div[2]/div/fieldset[2]/div/label[3]"
vnoofcarinputbox="//input[@id='vertical-spinner']"
vspinnerup = "//*[@id='content']/div[2]/div/fieldset[2]/div/span[2]/a[1]/span[1]"
vspinnerdown ="//*[@id='content']/div[2]/div/fieldset[2]/div/span[2]/a[2]/span[1]"
vbooknow="//button[@id='book']"

Openchrome.find_element_by_xpath("//span[@id='car-type-button']//span[@class='ui-selectmenu-icon ui-icon ui-icon-triangle-1-s']").click()
time.sleep(3)
Openchrome.find_element_by_xpath("//div[@id='ui-id-4']").click()
# select = Select(Openchrome.find_element_by_xpath(cartype))
# select.select_by_visible_text("SUV")
time.sleep(3)
Openchrome.find_element_by_xpath(standardradiobutton).click()
time.sleep(5)
Openchrome.find_element_by_xpath(automaticradiobutton).click()
Openchrome.find_element_by_xpath(insurancecheckbox).click()
Openchrome.find_element_by_xpath(noofcarinputbox).send_keys("2")
Openchrome.find_element_by_xpath(booknow).click()

Openchrome.find_element_by_xpath("//span[@id='ui-id-8-button']//span[@class='ui-selectmenu-icon ui-icon ui-icon-triangle-1-s']").click()
time.sleep(3)
Openchrome.find_element_by_xpath("//div[@id='ui-id-12']").click()
time.sleep(3)
Openchrome.find_element_by_xpath(vautomaticradiobutton).click()
time.sleep(5)
Openchrome.find_element_by_xpath(vstandardradiobutton).click()
Openchrome.find_element_by_xpath(vinsurancecheckbox).click()
Openchrome.find_element_by_xpath(vnoofcarinputbox).send_keys("5")
Openchrome.find_element_by_xpath(vbooknow)

# Using Sprinner -------------------


Openchrome.find_element_by_xpath(noofcarinputbox).clear()
numberofcars = 5
for cars in range(1,numberofcars+1):
    Openchrome.find_element_by_xpath(spinnerup).click()

Openchrome.find_element_by_xpath(vnoofcarinputbox).clear()
for cars in range(1,numberofcars+1):
    Openchrome.find_element_by_xpath(vspinnerup).click()

