from selenium import webdriver
import time
from selenium.webdriver import ActionChains

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//li[10]//a[1]").click()
time.sleep(5)
action=ActionChains(Openchrome)
tooltip=Openchrome.find_element_by_id("age")
msg = tooltip.get_attribute("title")
print (msg)
action.move_to_element(tooltip).perform()


