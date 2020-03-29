from selenium import webdriver
import time
from selenium.webdriver import ActionChains

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//aside[@class='widget']//a[contains(text(),'Tooltip and Double click')]").click()
time.sleep(5)
action=ActionChains(Openchrome)
tooltip=Openchrome.find_element_by_xpath("//div[@id='tooltipDemo']")
action.move_to_element(tooltip).perform()
msg = Openchrome.find_element_by_xpath("//span[@class='tooltiptext']").text
print(msg)


