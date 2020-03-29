from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Droppable')]").click()
takeaction = ActionChains(Openchrome)
Source = Openchrome.find_element_by_xpath("//div[@id='draggable']")
target = Openchrome.find_element_by_xpath("//div[@id='droppable']")
takeaction.drag_and_drop(Source,target).perform()
Openchrome.save_screenshot("dragdrop.png")

