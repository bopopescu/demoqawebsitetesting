from selenium import webdriver
import time

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
# Openchrome.maximize_window()

Openchrome.find_element_by_xpath("//a[contains(text(),'Spinner')]").click()
time.sleep(3)
spinner = Openchrome.find_element_by_xpath("//input[@id='spinner']")
up = Openchrome.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/p[1]/span[1]/a[1]/span[1]")
down = Openchrome.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/p[1]/span[1]/a[2]/span[1]")
number= input("please enter number ",)
number=int(number)
absnumber= abs(number)
spinner.clear()
spinner.send_keys(number)
time.sleep(3)
spinner.clear()
if number>0:
    for n in range(1,absnumber+1):
        up.click()
elif number<0:
    for n in range(1,absnumber+1):
        down.click()
elif number==0:
        down.click()
        up.click()

Openchrome.find_element_by_xpath("//button[@id='getvalue']").click()
alert = Openchrome.switch_to_alert()
msg = alert.text
print ("number on the spinner is", msg)
alert.accept()

# toggle enable and disable
time.sleep(5)
Openchrome.find_element_by_xpath("//button[@id='disable']").click()
#spinner.clear()
#spinner.send_keys(number)
time.sleep(5)
Openchrome.find_element_by_xpath("//button[@id='disable']").click()
# spinner.clear()

# Toggle Widget

Openchrome.find_element_by_xpath("//button[@id='destroy']").click()
spinner.clear()
spinner.send_keys(number)
time.sleep(10)

Openchrome.find_element_by_xpath("//button[@id='destroy']").click()
spinner.clear()
spinner.send_keys(number)









