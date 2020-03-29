from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Resizable')]").click()
resize = Openchrome.find_element_by_xpath("//*[@id='resizable']/div[3]")
takeaction = ActionChains(Openchrome)

takeaction.move_to_element(resize).click().drag_and_drop_by_offset(resize,-30,-30).perform()
Openchrome.save_screenshot(".//Screenshots/resize1.png")
time.sleep(3)
takeaction.move_to_element(resize).click().drag_and_drop_by_offset(resize,30,30).perform()
Openchrome.save_screenshot(".//Screenshots/resize2.png")
time.sleep(3)
takeaction.move_to_element(resize).click().drag_and_drop_by_offset(resize,30,-30).perform()
Openchrome.save_screenshot(".//Screenshots/resize3.png")
time.sleep(3)
