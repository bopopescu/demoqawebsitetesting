from selenium import webdriver
import time

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
Openchrome.maximize_window()


Openchrome.find_element_by_xpath("//a[contains(text(),'Progressbar')]").click()
msg = Openchrome.find_element_by_xpath("//*[@id='progressbar']/div").get_attribute("Style")
# print(msg)
msglist=msg.split(":")
# print(msglist)
print ("Progress Bar is at",msglist[1])