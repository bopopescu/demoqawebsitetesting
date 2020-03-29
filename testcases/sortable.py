from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class testdemoqa:
    Openchrome = webdriver.Chrome()
    Openchrome.get("https://demoqa.com/")
    Openchrome.maximize_window()
    def Testdraganddrop(self):
        self.Openchrome.find_element_by_xpath("//a[contains(text(),'Sortable')]").click()
        item1=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 1')]")
        item2=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 2')]")
        item3=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 3')]")
        item4=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 4')]")
        item5=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 5')]")
        item6=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 6')]")
        item7=self.Openchrome.find_element_by_xpath("//li[contains(text(),'Item 7')]")
        takeaction = ActionChains(self.Openchrome)
        takeaction.drag_and_drop(item7,item2).perform()
        takeaction.drag_and_drop(item1,item2).perform()
        takeaction.drag_and_drop(item1,item6).perform()
        takeaction.drag_and_drop(item3,item6).perform()
        takeaction.drag_and_drop(item5,item7).perform()
        takeaction.drag_and_drop(item7,item2).perform()
        takeaction.drag_and_drop(item6,item1).perform()

