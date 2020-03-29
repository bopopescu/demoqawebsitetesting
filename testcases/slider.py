from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Slider')]").click()
slider = Openchrome.find_element_by_xpath("//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
takeaction = ActionChains(Openchrome)

takeaction.move_to_element(slider).click().drag_and_drop_by_offset(slider,30,0).perform()
Openchrome.save_screenshot("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\Screenshots1\\slider1.png")
time.sleep(3)
takeaction.move_to_element(slider).click().drag_and_drop_by_offset(slider,60,0).perform()
Openchrome.save_screenshot("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\Screenshots1\\slider2.png")
time.sleep(3)
takeaction.move_to_element(slider).click().drag_and_drop_by_offset(slider,-30,0).perform()
Openchrome.save_screenshot("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\Screenshots1\\slider3.png")
time.sleep(3)
