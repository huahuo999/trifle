from tkinter import *
import undetected_chromedriver.v2 as uc
from time import sleep
from selenium.webdriver.support.ui import Select


def chooseSeat():
    user = entry1.get()
    password = entry2.get()
    date = entry3.get()
    startHour = entry4.get()
    startMinute = entry5.get()
    endHour = entry6.get()
    endMinute = entry7.get()

    browser = uc.Chrome()
    browser.get("http://zuowei.lixin.edu.cn/ClientWeb/xcus/ic2/Default.aspx")

    login_Element = browser.find_element_by_xpath("/html/body/header/div/nav/ul/li[5]/a/span")
    login_Element.click()
    sleep(1)

    users = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input")
    users.send_keys(user)
    sleep(1)

    psw = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input")
    psw.send_keys(password)
    sleep(1)

    submit = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[3]/input[1]")
    submit.click()
    sleep(1)

    thirdFloor = browser.find_element_by_xpath(
        '/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[10]/a')
    thirdFloor.click()
    sleep(3)

    c2 = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[10]/ul/li[1]/a")
    c2.click()
    sleep(2)

    chooseDate = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input")
    chooseDate.click()
    sleep(0.5)

    date = browser.find_element_by_xpath("//a[text()='{}']".format(date))
    date.click()
    sleep(0.5)

    startTime = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[1]")
    startTime.click()
    sleep(0.5)

    startHourSelect = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[2]/div/select")
    select = Select(startHourSelect)
    select.select_by_visible_text("{}".format(startHour))

    startMinuteSelect = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[3]/div/select")
    selectStartMinute = Select(startMinuteSelect)
    selectStartMinute.select_by_visible_text("{}".format(startMinute))

    endTime = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[2]")
    endTime.click()
    sleep(0.5)

    endhourSelect = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[2]/div/select")
    selectEnd = Select(endhourSelect)
    selectEnd.select_by_visible_text("{}".format(endHour))

    endMinuteSelect = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[3]/div/select")
    selectEndMinute = Select(endMinuteSelect)
    selectEndMinute.select_by_visible_text("{}".format(endMinute))

    submitTime = browser.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]")
    submitTime.click()
    sleep(0.5)

    seat = browser.find_element_by_xpath(
        "/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div[3]/div[92]")
    seat.click()
    sleep(2)

    ultimateTime = browser.find_element_by_xpath(
        "/html/body/div[8]/div[2]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[3]/select")
    ultimateTime.click()
    sleep(1)

    ultimateTimeSelect = Select(ultimateTime)
    ultimateTimeSelect.select_by_visible_text("{}".format("13:00"))

    submitSeat = browser.find_element_by_xpath("/html/body/div[8]/div[2]/form/div[2]/input[1]")
    submitSeat.click()
    sleep(1)


if __name__ == '__main__':
    # 初始化Tk()
    myWindow = Tk()
    # 设置标题
    myWindow.title('立信图书馆预约')
    # 标签控件布局
    Label(myWindow, text="user").grid(row=0)
    Label(myWindow, text="password").grid(row=1)
    Label(myWindow, text="date").grid(row=2)
    Label(myWindow, text="startHour").grid(row=3)
    Label(myWindow, text="startMinute").grid(row=4)
    Label(myWindow, text="endHour").grid(row=5)
    Label(myWindow, text="endMinute").grid(row=6)

    entry1 = Entry(myWindow)
    entry2 = Entry(myWindow)
    entry3 = Entry(myWindow)
    entry4 = Entry(myWindow)
    entry5 = Entry(myWindow)
    entry6 = Entry(myWindow)
    entry7 = Entry(myWindow)

    entry1.grid(row=0, column=1)
    entry1.insert(0, "201340216")

    entry2.grid(row=1, column=1)
    entry2.insert(0, "172821")

    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    entry6.grid(row=5, column=1)
    entry7.grid(row=6, column=1)

    Button(myWindow, text='Quit', command=myWindow.quit).grid(row=7, column=0, sticky=W, padx=5, pady=5)
    Button(myWindow, text='Run', command=chooseSeat).grid(row=7, column=1, sticky=W, padx=5, pady=5)
    # 进入消息循环
    myWindow.mainloop()
