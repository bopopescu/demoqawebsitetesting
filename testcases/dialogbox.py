from selenium import webdriver
import time
from selenium.webdriver import ActionChains

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
# Openchrome.maximize_window()


Openchrome.find_element_by_xpath("//a[contains(text(),'Dialog')]").click()
dialogbox = Openchrome.find_element_by_xpath("//div[@class='ui-dialog-titlebar ui-corner-all ui-widget-header ui-helper-clearfix ui-draggable-handle']")
dialogboxtext = Openchrome.find_element_by_xpath("//p[contains(text(),'This is the default dialog which is useful for dis')]").text
xbutton = Openchrome.find_element_by_xpath("//span[@class='ui-button-icon ui-icon ui-icon-closethick']")
topleftcorner = Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-nw']")
toprightcorner = Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-ne']")
bottomleftcorner = Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-sw']")
bottomrightcorner = Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
top= Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-n']")
right=Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-e']")
bottom= Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-s']")
left=Openchrome.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-w']")
action = ActionChains(Openchrome)
print("trying dragging the dialog box")
action.drag_and_drop_by_offset(dialogbox,10,20).perform()
action.drag_and_drop_by_offset(dialogbox,100,50).perform()
# action.drag_and_drop_by_offset(dialogbox,100,10).perform()
time.sleep(10)
print(dialogboxtext)
print("trying resize from top left corner")
action.move_to_element(topleftcorner).click_and_hold().move_by_offset(20,30).release(topleftcorner).perform()
time.sleep(10)
print("trying resize from top right corner")
action.move_to_element(toprightcorner).click_and_hold().move_by_offset(20,30).release(toprightcorner).perform()
time.sleep(10)
print("trying resize from bottom left corner")
action.move_to_element(bottomleftcorner).click_and_hold().move_by_offset(-20,-30).release(bottomleftcorner).perform()
time.sleep(10)
print("trying resize from bottom right corner")
action.move_to_element(bottomrightcorner).click_and_hold().move_by_offset(-20,3-0).release(bottomrightcorner).perform()
time.sleep(10)
print("trying resize by left line")
action.move_to_element(left).click_and_hold().move_by_offset(30,0).release(left).perform()
time.sleep(10)
print("trying resize by right line")
action.move_to_element(right).click_and_hold().move_by_offset(-30,0).release(right).perform()
time.sleep(10)
print("trying resize by top line")
action.move_to_element(top).click_and_hold().move_by_offset(0,30).release(top).perform()
time.sleep(10)
print("trying resize by bottom line")
action.move_to_element(bottom).click_and_hold().move_by_offset(0,-20).release(bottom).perform()
#





