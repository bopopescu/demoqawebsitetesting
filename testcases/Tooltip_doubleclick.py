from selenium import webdriver
import time
from selenium.webdriver import ActionChains

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//aside[@class='widget']//a[contains(text(),'Tooltip and Double click')]").click()
time.sleep(5)
double = Openchrome.find_element_by_xpath("//button[@id='doubleClickBtn']")
action=ActionChains(Openchrome)
action.double_click(double).perform()
alert = Openchrome.switch_to_alert()
time.sleep(3)
msg = alert.text
print(msg)
alert.accept()



