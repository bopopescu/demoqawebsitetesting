from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from datetime import date
from Utilities import xlutils
from Utilities.dateconverter import Date_spilt

Openchrome = webdriver.Chrome()
Openchrome.get("https://demoqa.com")
# Openchrome.maximize_window()

# ----------------if sendkeys works---------------------
Openchrome.find_element_by_xpath("//a[contains(text(),'Datepicker')]").click()
Openchrome.find_element_by_xpath("//input[@id='datepicker']").send_keys("12/25/2019")
Openchrome.find_element_by_xpath("//div[@id='content']").click()

Openchrome.find_element_by_xpath("//input[@id='datepicker']").clear()
Openchrome.find_element_by_xpath("//div[@id='content']").click()

# if send_Keys does not work ------------------------------------

dateinputbox_xpath="//input[@id='datepicker']"
month_xpath="//span[@class='ui-datepicker-month']"
year_xpath="//span[@class='ui-datepicker-year']"
leftclick_xpath="//span[@class='ui-icon ui-icon-circle-triangle-w']"
rightclick_xpath="//span[@class='ui-icon ui-icon-circle-triangle-e']"
table_xpath="//table[@class='ui-datepicker-calendar']"

Todaydate =date.today()
todaydate = Date_spilt.dateconverter(Todaydate)
todaydatestr=str(todaydate)
currentyear, currentmonth, currentday = map(int, todaydatestr.split('-'))
row = xlutils.getrowcount("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\data\\dates.xlsx","Sheet1")
for r in range(1,row+1):
    Inputdate = xlutils.readfromxl("C:\\Users\\Ramya\\PycharmProjects\\demoqa practice\\data\\dates.xlsx","Sheet1",r,1)
    inputdate = Date_spilt.dateconverter(Inputdate)
    inputdatestr= str(inputdate)
    inputyear, inputmonth, inputday = map(int, inputdatestr.split('-'))
    inputyear=str(inputyear)
    inputday=str(inputday)
    inputmonth=Date_spilt.month_numbertostring(inputmonth)
    if inputdate > todaydate:
        print("Future date -",inputdate)
        Openchrome.find_element_by_xpath(dateinputbox_xpath).click()
        time.sleep(3)
        while True:
            CurrentMonth = Openchrome.find_element_by_xpath(month_xpath).text
            CurrentYear = Openchrome.find_element_by_xpath(year_xpath).text
        # print(CurrentMonth,CurrentYear)
            if(CurrentMonth== inputmonth and CurrentYear==inputyear):
                break
            else:
                Openchrome.find_element_by_xpath(rightclick_xpath).click()
        dates=Openchrome.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")
        for dt in dates:
            #time.sleep(2)
            date1=dt.text
            if dt.text==inputday:
                dt.click()
                break
    elif inputdate < todaydate:
        print("past Date-",inputdate)
        Openchrome.find_element_by_xpath(dateinputbox_xpath).click()
        time.sleep(3)
        while True:
            CurrentMonth = Openchrome.find_element_by_xpath(month_xpath).text
            CurrentYear = Openchrome.find_element_by_xpath(year_xpath).text
            #print(CurrentMonth,inputmonth,CurrentYear,inputyear)
            if(CurrentMonth== inputmonth and CurrentYear==inputyear):
                break
            else:
                Openchrome.find_element_by_xpath(leftclick_xpath).click()
        dates=Openchrome.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")
        for dt in dates:
            #time.sleep(2)
            date1=dt.text
            #print(date1)
            if date1==inputday:
                dt.click()
                break
    elif inputdate == todaydate:
        print ("Today date-",inputdate)
        Openchrome.find_element_by_xpath(dateinputbox_xpath).click()
        dates = Openchrome.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")
        for dt in dates:
            date1=dt.text
            #print(date1)
            if date1 == inputday:
                dt.click()
                break
    time.sleep(10)
    filename="C:\\Users\Ramya\\PycharmProjects\\demoqa practice\\Screenshots1\\screenshot_"+ inputdate+".png"
    print(filename)
    Openchrome.save_screenshot(filename)
    Openchrome.find_element_by_xpath(dateinputbox_xpath).clear()
    Openchrome.find_element_by_xpath("//div[@id='content']").click()


