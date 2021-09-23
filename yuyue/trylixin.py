import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support.ui import Select
from settings import USER_LS, PASSWORD_LS

browser = uc.Chrome()
browser.get("http://zuowei.lixin.edu.cn/ClientWeb/xcus/ic2/Default.aspx")
wait = WebDriverWait(browser, 20)

login_Element = browser.find_element_by_xpath("/html/body/header/div/nav/ul/li[5]/a/span")
login_Element.click()
sleep(1)

user = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input")
user.send_keys(USER_LS)
sleep(1)

psw = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input")
psw.send_keys(PASSWORD_LS)
sleep(1)

submit = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[3]/input[1]")
submit.click()
sleep(1)



thirdFloor = browser.find_element_by_xpath(
            '/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[10]/a')
thirdFloor.click()
sleep(3)

c2 = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[10]/ul/li[1]/a")
c2.click()
sleep(2)

chooseDate = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input")
chooseDate.click()
sleep(0.5)

date = browser.find_element_by_xpath("//a[text()='11']")
date.click()
sleep(0.5)


startTime = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[1]")
startTime.click()
sleep(0.5)

startHourSelect = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[2]/div/select")
select = Select(startHourSelect)
select.select_by_visible_text("08")

endTime = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/span[2]/input[2]")
endTime.click()
sleep(0.5)

endhourSelect = browser.find_element_by_xpath("/html/body/div[6]/div[2]/dl/dd[2]/div/select")
selectEnd = Select(endhourSelect)
selectEnd.select_by_visible_text("22")

submitTime = browser.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]")
submitTime.click()
sleep(0.5)

seat = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div[3]/div[92]")
seat.click()
sleep(2)

submitSeat = browser.find_element_by_xpath("/html/body/div[8]/div[2]/form/div[2]/input[1]")
submitSeat.click()
sleep(1)
