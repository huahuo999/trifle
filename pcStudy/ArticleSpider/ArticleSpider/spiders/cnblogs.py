from urllib import parse
import json
import re

import scrapy
import undetected_chromedriver.v2 as uc
from scrapy import Request
from scrapy.loader import ItemLoader
import requests

from ArticleSpider.items import CnblogsArticleItem
from ArticleSpider.utils import common
from ArticleSpider.items import ArticleItemLoader

# 模拟浏览器

class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']
    custom_settings = {
        "COOKIES_ENABLED": True
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
            # 将cookie交给scrapy,由于后续请求不会沿用之前请求的cookie
            # 要使用    custom_settings = {
            #         "COOKIES-ENABLED": True
            #     }
        for url in self.start_urls:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
            }
            yield scrapy.Request(url, cookies=cookie_dict, headers=headers, dont_filter=True)
        pass

    def parse(self, response):
        """
        1. 获取新闻列表页中的新闻url并交给scrapy进行下载后调用相应的解析方法
        2. 获取下一页的url并交给scrapy进行下载，下载完成后交给parse继续跟进
        :param response:
        :return:
        """
        post_nodes = response.css('.news_block')
        for post_node in post_nodes:
            img_url = post_node.css('.entry_summary a img::attr(src)').extract_first("")
            if "https" not in img_url:
                img_url = "https:" + post_node.css('.entry_summary a img::attr(src)').extract_first("")
                # img_url 没有https无法访问
            post_url = post_node.css('h2 a::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": img_url},
                          callback=self.parse_detail)
            # 如果post_url不全 就从response.url提取域名
            # 如果全就不提取
            # 使用yield之后会立马交给scrapy下载 相当于不会断掉的return
            # callback默认值为parse 相当于深度优先不停的调用parse

        # 提取下一页并交给scrapy进行下载
        # next_url = response.css("div.pager a:last-child::text").extract_first()
        # if next_url == "Next >":
        #     next_url = response.css("div.pager a:last-child::attr(href)").extract_first()
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        match_re = re.match(".*?(\d+)", response.url)
        if match_re:
            post_id = match_re.group(1)
            # article_item = CnblogsArticleItem()
            #
            # title = response.css("#news_title a::text").extract_first()
            # create_date = response.css("#news_info .time::text").extract_first()
            #
            # match_re = re.match(".*?(\d+.*)", create_date)
            # if match_re:
            #     create_date = match_re.group(1)
            # content = response.css("#news_content").extract()[0]
            # tag_list = response.css(".news_tags a::text").extract()
            # tags = ",".join(tag_list)
            # # 将tags用,连在一起方便储存
            #
            # article_item["title"] = title
            # article_item["create_date"] = create_date
            # article_item["content"] = content
            # article_item["tags"] = tags
            # article_item["url"] = response.url
            # article_item["front_image_url"] = [response.meta.get("front_image_url", "")]
            # if response.meta.get("front_image_url", ""):
            #     article_item["front_image_url"] = [response.meta.get("front_image_url", "")]
            # else:
            #     article_item["front_image_url"] = []
            # scrapy要求这个地方下载图片的url必须是个list
            # 使用get方法防止抛出异常

            item_loader = ArticleItemLoader(item=CnblogsArticleItem(), response=response)
            # 默认的类型是list类型
            item_loader.add_css("title", "#news_title a::text")
            item_loader.add_css("content", "#news_content")
            item_loader.add_css("tags", ".news_tags a::text")
            item_loader.add_css("create_date", "#news_info .time::text")
            item_loader.add_value("url", response.url)
            if response.response.meta.get("front_image_url", []):
                item_loader.add_value("front_image_url", response.meta.get("front_image_url", []))



            yield Request(url=parse.urljoin(response.url, "/NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)),
                          meta={"article_item": item_loader, "url": response.url}, callback=self.parse_nums)
            # html = requests.get(
            #     url=parse.urljoin(response.url, "/NewsAjax/GetAjaxNewsInfo?contentId={}").format(post_id))
            # j_data = json.loads(html.text)
            # 最前面不加/ html会默认放在response.url的后面
            # 加了/后会放在域名后面

            # praise_nums = j_data['DiggCount']
            # fav_nums = j_data['TotalView']
            # comment_nums = j_data['CommentCount']
            pass

    def parse_nums(selfs, response):
        j_data = json.loads(response.text)
        item_loader = response.meta.get("article_item", "")

        item_loader.add_value("praise_nums", j_data['DiggCount'])
        item_loader.add_value("fav_nums", j_data['TotalView'])
        item_loader.add_value("comment_nums", j_data['CommentCount'])
        item_loader.add_value("url_object_id", common.get_md5(response.meta.get("url", "")))
        article_item = item_loader.load_item()
        yield article_item
        # 如果yield request会进行下载
        # 如果yield item会进行pipeline处理
