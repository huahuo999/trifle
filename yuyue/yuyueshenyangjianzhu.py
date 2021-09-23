import datetime
from tkinter import *

import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.ui import Select
from time import sleep


def check():
    hour = -1
    browser = uc.Chrome()
    browser1 = uc.Chrome()
    while hour != 0:
        i = datetime.datetime.now()
        print(i)
        sleep(5)
        print("当前hour", i.hour)
        print("循环第{}次".format(i.second))
        hour = i.hour
    now = datetime.datetime.now()
    chooseSeat(now.day + 1, browser, "1803200402", "333333", "08", "30")
    chooseSeat(now.day + 1, browser1, '1803200333', "333333", "16", "30")


def chooseSeat(date, browser, user, password, startTimeHour, startTimeMinute):
    browser.get("http://libseat.sjzu.edu.cn/ClientWeb/xcus/ic2/Default.aspx")
    loginHomeElement = browser.find_element_by_xpath("/html/body/header/div/nav/ul/li[5]/a")
    loginHomeElement.click()
    sleep(1)

    users = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input")
    users.send_keys(user)

    pwd = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input")
    pwd.send_keys(password)
    sleep(0.5)

    submit = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[3]/input[1]")
    submit.click()
    sleep(1)

    fiveFloor = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[5]/a")
    fiveFloor.click()
    sleep(0.5)

    sixteenSection = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[5]/ul/li[1]/a")
    sixteenSection.click()
    sleep(3)

    chooseDate = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input")
    chooseDate.click()
    sleep(0.5)

    date = browser.find_element_by_xpath("//a[text()='{}']".format(date))
    date.click()
    sleep(0.5)

    startTimeElement = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[1]")
    startTimeElement.click()
    sleep(0.5)

    startTimeHourElement = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[2]/div/select")
    startTimeHourSelect = Select(startTimeHourElement)
    startTimeHourSelect.select_by_visible_text(startTimeHour)
    sleep(1)

    startTimeMinuteElement = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[3]/div/select")
    startTimeMinuteSelect = Select(startTimeMinuteElement)
    startTimeMinuteSelect.select_by_visible_text(startTimeMinute)
    sleep(1)

    seat28 = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div[3]/div[28]")
    browser.execute_script("arguments[0].click();", seat28)
    sleep(0.5)

    submit = browser.find_element_by_xpath("/html/body/div[8]/div[2]/form/div[2]/input[1]")
    submit.click()
    sleep(0.5)


if __name__ == '__main__':
    myWindow = Tk()
    myWindow.title('沈阳建筑大学预约')
    Label(myWindow, text="当前状态").grid(row=0)
    entry1 = Entry(myWindow)
    entry1.insert(0, "若已经到时间,点击run后请等待1min")
    entry1.grid(row=0, column=1)
    Button(myWindow, text='Quit', command=myWindow.quit).grid(row=1, column=0, sticky=W, padx=5, pady=5)
    Button(myWindow, text='Run', command=check).grid(row=1, column=1, sticky=W, padx=5, pady=5)
    # 进入消息循环
    myWindow.mainloop()

