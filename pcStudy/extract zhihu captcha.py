import requests
import undetected_chromedriver.v2 as uc
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By


class getZhihuCaptcha:
    def __init__(self, USER, PASSWORD, number):
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.browser = uc.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.criteria = number

    def download_Img(self, url):
        '''
        下载图片并保存
        :param url: 图片网址
        :return:
        '''
        try:
            response = requests.get(url)
        except Exception as e:
            print('图片下载失败')
            raise e
        else:
            filename = url.split('/')[3]
            with open('ZhihuCaptcha/{}'.format(filename), 'wb') as f:
                f.write(response.content)

    def start_Getting(self):

        self.browser.get("https://www.zhihu.com/")
        login_element = self.browser.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]')

        self.browser.execute_script("arguments[0].click();", login_element)

        # 输入账号
        username = self.wait.until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, '.SignFlow-account input'))
            # 等待可以点击
        )
        username.send_keys(self.USER)

        # 输入密码
        password = self.wait.until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, '.SignFlow-password input'))
            # 等待可以点击
        )
        password.send_keys(self.PASSWORD)
        time.sleep(4)

        # 点击提交
        submit = self.wait.until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, '.Button.SignFlow-submitButton'))
        )
        submit.click()
        time.sleep(3)

        tried = 0
        while tried <= self.criteria:

            bg_img = self.wait.until(
                Ec.presence_of_element_located((By.CSS_SELECTOR, '.yidun_bgimg .yidun_bg-img'))
            )
            background_url = bg_img.get_attribute('src')
            print("当前", background_url)
            self.download_Img(background_url)

            refresh = self.wait.until(
                Ec.element_to_be_clickable((By.CSS_SELECTOR, '.yidun_top .yidun_refresh'))
            )
            refresh.click()

            time.sleep(2)


    def __del__(self):
        self.browser.close()
        print('界面关闭')
        # self.display.stop()


if __name__ == '__main__':
    getZhihuCaptcha_test = getZhihuCaptcha("18117032558", "86697709p", 100)
    getZhihuCaptcha_test.start_Getting()
