from selenium import webdriver
import time

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com/")
Openchrome.maximize_window()
Openchrome.find_element_by_xpath("//a[contains(text(),'HTML contact form')]").click()
time.sleep(5)
Openchrome.find_element_by_css_selector("input[class=firstname").send_keys("test1")
Openchrome.find_element_by_id("lname").send_keys("test2")
Openchrome.find_element_by_name("country").send_keys("India")
Openchrome.find_element_by_name("subject").send_keys("Hope this is easy as it looks")
Openchrome.save_screenshot("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\Screenshots1\\htmlform.png")
time.sleep(3)
Openchrome.find_element_by_xpath("//input[4]").click()