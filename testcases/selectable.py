from selenium import webdriver
import time

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Selectable')]").click()

Openchrome.find_element_by_xpath("//li[contains(text(),'Item 1')]").click()
Openchrome.save_screenshot(".//Screenshots/select1.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//li[contains(text(),'Item 2')]").click()
Openchrome.save_screenshot(".//Screenshots/select2.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//li[contains(text(),'Item 3')]").click()
Openchrome.save_screenshot(".//Screenshots/select3.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//li[contains(text(),'Item 4')]").click()
Openchrome.save_screenshot(".//Screenshots/select4.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//li[contains(text(),'Item 5')]").click()
Openchrome.save_screenshot(".//Screenshots/select5.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//li[contains(text(),'Item 6')]").click()
Openchrome.save_screenshot(".//Screenshots/select6.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//li[contains(text(),'Item 7')]").click()
Openchrome.save_screenshot(".//Screenshots/select7.png")
time.sleep(3)