from django.db import models

# Create your models here.
"""
1.我们的模型类需要继承自 models.Model
2.系统会自动化为我们添加一个主键---id
3.字段=model.类型（选项）
字段名其实就是数据表的字段名
char(M) M就是选项

一定要注册子应用

"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)








