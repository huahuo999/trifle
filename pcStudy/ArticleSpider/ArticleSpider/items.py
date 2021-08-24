# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst, Identity, Join
from scrapy.loader import ItemLoader
class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def date_convert(value):
    match_re = re.match(".*?(\d+.*)", value)
    if match_re:
        return match_re.group(1)
    else:
        # 防止报错
        return "1970-07-01"

class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    # 只想要第一个


class CnblogsArticleItem(scrapy.Item):
    # input_processor 当管道刚传进来item的时候先进行第一步处理
    # output_processor 控制传出管道时候的数据类型 identity就保持原有的list takefirst是从list中提取出来str
    title = scrapy.Field(
        # input_processor = MapCompose(add_Cnblog),
        # MapCompose是用来处理item的某个变量的 可以赋给多个函数
    )
    # 标题
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    # 创建时间
    url = scrapy.Field()
    # url
    url_object_id = scrapy.Field()
    # 由于url过长,md5生成
    front_image_url = scrapy.Field(
        output_processor=Identity()
        # 如果都用TakeFirst会变成str,但下载图片的时候必须是list所以用Identity()保持原样
    )
    # 自动下载字段
    front_image_path = scrapy.Field()
    # 图片地址
    praise_nums = scrapy.Field()
    # 点赞数目
    comment_nums = scrapy.Field()
    # 评论数目
    fav_nums = scrapy.Field()
    # 查看数目
    tags = scrapy.Field(
        output_processor=Join(separator=",")
        # Join将list全部用，隔开
    )
    # 标签
    content = scrapy.Field()
    # 内容

