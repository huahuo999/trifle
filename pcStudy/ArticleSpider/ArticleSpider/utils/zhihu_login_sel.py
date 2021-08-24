import json
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import os
import random
import cv2
import numpy as np
import undetected_chromedriver.v2 as uc


from ArticleSpider.settings import  BAIDU_AK, BAIDU_SK

class Code():
    '''
    滑动验证码破解
    '''

    def __init__(self, slider_ele=None, background_ele=None, count=1, save_image=False):
        '''

        :param slider_ele:
        :param background_ele:
        :param count:  验证重试次数
        :param save_image:  是否保存验证中产生的图片， 默认 不保存
        '''

        self.count = count
        self.save_images = save_image
        self.slider_ele = slider_ele
        self.background_ele = background_ele

    def get_slide_locus(self, distance):
        distance += 8
        v = 0
        m = 0.3
        # 保存0.3内的位移
        tracks = []
        current = 0
        mid = distance * 4 / 5
        while current <= distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            s = v0 * m + 0.5 * a * (m ** 2)
            current += s
            tracks.append(round(s))
            v = v0 + a * m
        return tracks

    def slide_verification(self, driver, slide_element, distance):
        '''

        :param driver: driver对象
        :param slide_element: 滑块元祖
        :type   webelement
        :param distance: 滑动距离
        :type: int
        :return:
        '''
        # 获取滑动前页面的url网址
        start_url = driver.current_url
        print('滑动距离是: ', distance)
        # 根据滑动的距离生成滑动轨迹
        locus = self.get_slide_locus(distance)

        print('生成的滑动轨迹为:{},轨迹的距离之和为{}'.format(locus, distance))

        # 按下鼠标左键
        ActionChains(driver).click_and_hold(slide_element).perform()

        time.sleep(0.5)

        # 遍历轨迹进行滑动
        for loc in locus:
            time.sleep(0.01)
            # 此处记得修改scrapy的源码 selenium\webdriver\common\actions\pointer_input.py中将DEFAULT_MOVE_DURATION改为50，否则滑动很慢
            ActionChains(driver).move_by_offset(loc, random.randint(-5, 5)).perform()
            ActionChains(driver).context_click(slide_element)

        # 释放鼠标
        ActionChains(driver).release(on_element=slide_element).perform()

    def onload_save_img(self, url, filename="image.png"):
        '''
        下载图片并保存
        :param url: 图片网址
        :param filename: 图片名称
        :return:
        '''
        try:
            response = requests.get(url)
        except Exception as e:
            print('图片下载失败')
            raise e
        else:
            with open(filename, 'wb') as f:
                f.write(response.content)

    def image_crop(self, image, loc):
        cv2.rectangle(image, loc[0], loc[1], (7, 249, 151), 2)
        cv2.imshow('Show', image)
        # cv2.imshow('Show2', slider_pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class Login(object):
    def __init__(self, user, password, retry):
        # self.display = Display(visible=0, size=(800, 800))
        # self.display.start()
        # 创建一个参数对象，用来控制chrome以无界面模式打开
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')  # # 浏览器不提供可视化页面
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速,GPU加速可能会导致Chrome出现黑屏，且CPU占用率高达80%以上
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.browser = uc.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.url = 'https://www.zhihu.com/signin'
        self.sli = Code()
        self.user = user
        self.password = password
        self.retry = retry  # 重试次数

    def login_baidu(self):
        # 请求网址
        self.browser.get(self.url)
        # 点击输入密码界面
        # login_status = self.wait.until(
        #     Ec.presence_of_element_located((By.XPATH, '//div[@class="switch-type"]'))
        # )
        # login_status.click()

        self.browser.get(self.url)
        login_element = self.browser.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]')

        self.browser.execute_script("arguments[0].click();", login_element)
        time.sleep(5)

        # 输入账号
        username = self.wait.until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, '.SignFlow-account input'))
        )
        username.send_keys(self.user)
        # 输入密码
        password = self.wait.until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, '.SignFlow-password input'))
        )
        password.send_keys(self.password)

        # 登录框
        submit = self.wait.until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, '.Button.SignFlow-submitButton'))
        )
        submit.click()
        time.sleep(3)

        k = 1
        # while True:
        while k < self.retry:
            bg_img = self.wait.until(
                Ec.presence_of_element_located((By.CSS_SELECTOR, '.yidun_bgimg .yidun_bg-img'))
            )
            background_url = bg_img.get_attribute('src')
            backgroundFilename = "background.jpg"
            self.sli.onload_save_img(background_url, backgroundFilename)
            baidu = BaiDuLogin(BAIDU_AK, BAIDU_SK)

            # 获取验证码滑动距离
            distance = baidu.recognize(backgroundFilename)
            print('滑动距离是', distance)

            # 2. 乘缩放比例， -去  滑块前面的距离  下面给介绍
            distance = distance - 4
            print('实际滑动距离是', distance)

            # 滑块对象
            element = self.browser.find_element_by_css_selector(
                '.yidun_slider')
            # 滑动函数
            self.sli.slide_verification(self.browser, element, distance)

            # 滑动之后的url链接
            time.sleep(5)
            # 登录框
            try:
                submit = self.wait.until(
                    Ec.element_to_be_clickable((By.CSS_SELECTOR, '.Button.SignFlow-submitButton'))
                )
                submit.click()
                time.sleep(3)
            except:
                pass

            end_url = self.browser.current_url
            print(end_url)

            if end_url == "https://www.zhihu.com/":
                os.remove(backgroundFilename)
                return self.get_cookies()
            else:
                time.sleep(3)

                k += 1

        return None


    def get_cookies(self):
        '''
        登录成功后 保存账号的cookies
        :return:
        '''
        cookies = self.browser.get_cookies()
        self.cookies = ''
        for cookie in cookies:
            self.cookies += '{}={};'.format(cookie.get('name'), cookie.get('value'))
        return cookies

    def __del__(self):
        self.browser.close()
        print('界面关闭')
        # self.display.stop()


class BaiDuLogin():
    def __init__(self, ak, sk):
        self.ak = ak
        self.sk = sk

    def get_access_token(self):
        import requests
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type' \
               '=client_credentials&client_id={}&client_secret={}'.format(self.ak, self.sk)
        response = requests.get(host)
        if response.status_code == 200:
            return response.json()["access_token"]
        return None

    def recognize(self, image_file):
        ACCESS_TOKEN = self.get_access_token()
        # 获取ACCESS_TOKEN

        with open(image_file, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            base64_str = base64_data.decode('UTF8')
        # 按照图片路径打开图片并转换为base64格式

        PARAMS = {"image": base64_str}
        MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/lszhihu"
        request_url = "{}?access_token={}".format(MODEL_API_URL, ACCESS_TOKEN)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=request_url, json=PARAMS, headers=headers)
        response_json = response.json()
        if "results" not in response_json:
            return None
        if len(response_json["results"]) == 0:
            return None
        if "location" not in response_json["results"][0]:
            return None
        return response_json['results'][0]["location"]["left"]

