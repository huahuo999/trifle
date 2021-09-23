import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep


browser = uc.Chrome()
browser.get("http://libseat.sjzu.edu.cn/ClientWeb/xcus/ic2/Default.aspx")
wait = WebDriverWait(browser, 20)

login_Element = browser.find_element_by_xpath("/html/body/header/div/nav/ul/li[5]/a")
login_Element.click()
sleep(1)

user = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input")
user.send_keys("1803200402")
sleep(1)

pwd = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input")
pwd.send_keys("333333")
sleep(1)

submit = browser.find_element_by_xpath("/html/body/div[7]/div[2]/form/div[1]/div[3]/input[1]")
submit.click()
sleep(1)


fiveFloor = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[5]/a")
fiveFloor.click()
sleep(0.5)

sixteenSection = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[1]/div/div/div/div[4]/ul/li[5]/ul/li[1]/a")
sixteenSection.click()
sleep(3)

chooseDate = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/span[1]/input")
chooseDate.click()
sleep(0.5)

date = browser.find_element_by_xpath("//a[text()='10']")
date.click()
sleep(0.5)

twentyEight = browser.find_element_by_xpath("/html/body/div[5]/div/table/tbody/tr/td[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div[3]/div[28]")
twentyEight.click()
sleep(1)

startTime = browser.find_element_by_xpath("/html/body/div[8]/div[2]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[1]/select[1]")
startTime.click()
sleep(0.5)
Select(browser.find_element_by_name("start_time")).select_by_value("900")

endTime = browser.find_element_by_xpath("/html/body/div[9]/div[2]/form/div[1]/table/tbody[2]/tr[2]/td[2]/div/span[3]/select")
endTime.click()
sleep(0.5)
Select(browser.find_element_by_name("start_time")).select_by_value("1300")

submitseat = browser.find_element_by_xpath("/html/body/div[8]/div[2]/form/div[2]/input[1]")
submitseat.click()
sleep(0.5)


