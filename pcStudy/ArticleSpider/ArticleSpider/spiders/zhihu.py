
from ArticleSpider.utils import zhihu_login_sel
from ArticleSpider.settings import USER, PASSWORD
import  scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    custom_settings = {
        "COOKIES_ENABLED": True
        # 实现模拟登录必须
    }

    def start_requests(self):
        # 模拟登录拿到cookie
        # 如何识别滑动验证码:1.使用opencv
        # 使用机器学习方法识别
        l = zhihu_login_sel.Login(USER, PASSWORD, 6)
        cookie_dict = l.login()

        for url in self.start_urls:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
            }
            yield scrapy.Request(url, cookies=cookie_dict, headers=headers, dont_filter=True)

    def parse(self, response, **kwargs):
        pass