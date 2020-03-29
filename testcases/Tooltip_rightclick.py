from selenium import webdriver
import time
from selenium.webdriver import ActionChains

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//aside[@class='widget']//a[contains(text(),'Tooltip and Double click')]").click()
time.sleep(5)
action=ActionChains(Openchrome)
rightclick = Openchrome.find_element_by_id("rightClickBtn")
action.context_click(rightclick).perform()
edit = Openchrome.find_element_by_xpath("//div[contains(text(),'Edit this')]")
time.sleep(3)
action.move_to_element(edit).click().perform()
time.sleep(5)
alert1 = Openchrome.switch_to_alert()
msg1 = alert1.text
alert1.accept()
print(msg1)


