from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'IFrame practice page')]").click()

Openchrome.switch_to_frame("IF1")
#Openchrome.find_element_by_xpath("//span[class='menu-item-text']")

Openchrome.switch_to_default_content()

Openchrome.switch_to_frame("IF2")
# Openchrome.find_element_by_xpath("//*[@id='sidebar']/aside[1]/ul/li[1]/")
Openchrome.switch_to_default_content()