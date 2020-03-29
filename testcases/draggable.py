from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Draggable')]").click()
drag = Openchrome.find_element_by_xpath("//div[@id='draggable']")
takeaction = ActionChains(Openchrome)
takeaction.move_to_element(drag).click().drag_and_drop_by_offset(drag,40,40).perform()
Openchrome.save_screenshot(".\\Screenshots\\drag10.png")
takeaction.move_to_element(drag).click().drag_and_drop_by_offset(drag,-140,100).perform()
Openchrome.save_screenshot(".//Screenshots//drag2.png")