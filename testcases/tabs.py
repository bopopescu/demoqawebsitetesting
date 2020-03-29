from selenium import webdriver
import time

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Tabs')]").click()
time.sleep(3)
Openchrome.find_element_by_xpath("//a[@id='ui-id-1']").click()
msg =Openchrome.find_element_by_xpath("//p[contains(text(),'Proin elit arcu, rutrum commodo, vehicula tempus,')]").text
print (msg)
print()
time.sleep(3)
Openchrome.find_element_by_xpath("//a[@id='ui-id-2']").click()
msg=Openchrome.find_element_by_xpath("//p[contains(text(),'Morbi tincidunt, dui sit amet facilisis feugiat, o')]").text
print(msg)
print()
time.sleep(5)
Openchrome.find_element_by_xpath("//a[@id='ui-id-3']").click()
msg=Openchrome.find_element_by_xpath("//p[contains(text(),'Mauris eleifend est et turpis. Duis id erat. Suspe')]").text
msg1=Openchrome.find_element_by_xpath("//p[contains(text(),'Duis cursus. Maecenas ligula eros, blandit nec, ph')]").text
print(msg)
print()
print(msg1)
