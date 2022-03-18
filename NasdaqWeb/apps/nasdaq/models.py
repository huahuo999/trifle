from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Links(models.Model):
    source = models.CharField(db_column="s", max_length=255)  # s
    target = models.CharField(db_column="o", max_length=255)  # o
    name = models.CharField(db_column="p", max_length=255)  # p
    des = models.CharField(db_column="des", max_length=255) #

    class Meta:
        managed = True
        # 接收管理 自动映射到后台
        db_table = "graph"
        # 后台表名


class Nodes(models.Model):
    name = models.CharField(db_column="entity", max_length=255)
    des = models.CharField(db_column="des", max_length=255)
    symbolSize = models.IntegerField(db_column="symbolsize")
    category = models.IntegerField(db_column="depth")

    class Meta:
        managed = True
        # 接收管理 自动映射到后台
        db_table = "node"
        # 后台表名
