from selenium import webdriver
from selenium.webdriver import ActionChains
import time

Openchrome = webdriver.Chrome()

Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//aside[2]//ul[1]//li[1]//a[1]").click()
# Openchrome.find_element_by_xpath("//button[@id='button1']").click()
# Openchrome.find_element_by_xpath("//button[contains(text(),'New Message Window')]").click()
Openchrome.find_element_by_xpath("//button[contains(text(),'New Browser Tab')]").click()
time.sleep(5)
Handles= Openchrome.window_handles
for Handle in Handles:
    print(Handle)
    Openchrome.switch_to_window(Handle)
    title = Openchrome.title
    # body=Openchrome.find_element_by_tag_name("Body").text
    print(title)
    # print(body)

