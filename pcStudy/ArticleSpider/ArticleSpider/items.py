# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CnblogsArticleItem(scrapy.Item):
    title = scrapy.Field()
    # 标题
    create_date = scrapy.Field()
    # 创建时间
    url = scrapy.Field()
    # url
    url_object_id = scrapy.Field()
    # 由于url过长,md5生成
    front_image_url = scrapy.Field()
    # 自动下载字段
    front_image_path = scrapy.Field()
    # 图片地址
    praise_nums = scrapy.Field()
    # 点赞数目
    comment_nums = scrapy.Field()
    # 评论数目
    fav_nums = scrapy.Field()
    # 查看数目
    tags = scrapy.Field()
    # 标签
    content = scrapy.Field()
    # 内容
