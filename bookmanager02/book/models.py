from django.db import models

# Create your models here.
'''
1.模型类需要继承 models.Model
2.定义属性
    属性名=models.类型（选项）
    2.1 属性名 对应 字段名（不要使用python，mysql关键字，连续的__下划线）
    2.2 类型 mysql的类型
    2.3 选项 是否有默认值，是否唯一，是否为null
    CharField 必须设置max_length
3.修改表的名字
    默认名字是：子应用名_类名 都是小写
    修改表的名子
'''


class BookInfo(models.Model):
    # id自动添加
    name = models.CharField(max_length=10, unique=True)
    pub_data = models.DateField(True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字
        verbose_name = '书籍管理'  # admin站点的使用


class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    # 外键 关联的_id自动生成
    # SET_NULL 只在允许为空是使用
    # 抛出异常，不删除 PROTECT
    # 联级删除 CASCADE

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'peopleinfo'

