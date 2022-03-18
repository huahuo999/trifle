from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 加入相对路径
execute(["scrapy", "crawl", "cnblogs"])
# execute(["scrapy", "crawl", "zhihu"])
