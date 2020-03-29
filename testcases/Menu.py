from selenium import webdriver
import time
from selenium.webdriver import ActionChains

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
Openchrome.maximize_window()


Openchrome.find_element_by_xpath("//a[contains(text(),'Menu')]").click()
books = Openchrome.find_element_by_xpath("//div[@id='ui-id-2']")
clothing = Openchrome.find_element_by_xpath("//div[@id='ui-id-3']")
electronics = Openchrome.find_element_by_xpath("//div[@id='ui-id-4']")
carhifi=Openchrome.find_element_by_xpath("//div[@id='ui-id-6']")
utilities = Openchrome.find_element_by_xpath("//div[@id='ui-id-7']")
movies = Openchrome.find_element_by_xpath("//div[@id='ui-id-8']")
music = Openchrome.find_element_by_xpath("//div[@id='ui-id-9']")
rocks = Openchrome.find_element_by_xpath("//div[@id='ui-id-10']")
alternative = Openchrome.find_element_by_xpath("//div[@id='ui-id-11']")
classic = Openchrome.find_element_by_xpath("//div[@id='ui-id-12']")
jazz = Openchrome.find_element_by_xpath("//div[@id='ui-id-13']")
freejazz = Openchrome.find_element_by_xpath("//div[@id='ui-id-14']")
bigband=Openchrome.find_element_by_xpath("//div[@id='ui-id-15']")
modern=Openchrome.find_element_by_xpath("//div[@id='ui-id-16']")
pop=Openchrome.find_element_by_xpath("//div[@id='ui-id-17']")
action = ActionChains(Openchrome)

action.move_to_element(books).perform()
time.sleep(3)
action.move_to_element(clothing).perform()
action.move_to_element(electronics).click().move_to_element(carhifi).perform()
time.sleep(3)
action.move_to_element(electronics).click().move_to_element(utilities).perform()
time.sleep(3)
action.move_to_element(movies).perform()
time.sleep(3)
action.move_to_element(music).click().move_to_element(rocks).click().move_to_element(alternative).perform()
time.sleep(3)
action.move_to_element(music).click().move_to_element(rocks).click().move_to_element(classic).perform()
time.sleep(3)
action.move_to_element(music).click().move_to_element(jazz).click().move_to_element(freejazz).perform()
time.sleep(3)
action.move_to_element(music).click().move_to_element(jazz).click().move_to_element(bigband).perform()
time.sleep(3)
action.move_to_element(music).click().move_to_element(jazz).click().move_to_element(modern).perform()
time.sleep(3)
action.move_to_element(music).click().move_to_element(pop).perform()


