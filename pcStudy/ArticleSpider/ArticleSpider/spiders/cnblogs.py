import scrapy
import undetected_chromedriver.v2 as uc


# 模拟浏览器

class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']
    custom_settings = {
        "COOKIES-ENABLED": True
    }

    def start_requests(self):
        # 入口模拟登录拿到cookie
        browser = uc.Chrome()
        browser.get("https://account.cnblogs.com/signin")
        # 自动化输入，自动化识别滑动验证码并自动拖动
        input("回车继续:")
        cookie_dict = {}
        cookies = browser.get_cookies()
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
        for url in self.start_urls:
            # 将cookie交给scrapy,后续请求不会沿用之前请求的cookie
            # 要使用    custom_settings = {
            #         "COOKIES-ENABLED": True
            #     }
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
            }
            yield scrapy.Request(url, cookies=cookie_dict, headers=headers, dont_filter=True)
        pass

    def parse(self, response):
        url = response.css('div#news_list h2 a::attr(href)').extract()
        pass
