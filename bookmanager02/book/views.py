from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("hello,平凡")


# 增加数据
from book.models import BookInfo
# 方法一
book = BookInfo(
    name='Django',
    pub_data='2003-3-9',
    readcount=9
)
# 必须调用save才能保存到数据库
book.save()

# 方法二
BookInfo.objects.create(
    name='C++',
    pub_data='2022-7-24',
    readcount=15
)

# 修改数据
# 方式一
# select * from bookinfo where id = 6;
book = BookInfo.objects.get(id=6)
book.name = '大数据开发'
# 想要保存用对象的save 的方法
book.save()

# 方法二 filter过滤
BookInfo.objects.filter(id=5).update(name='爬虫入门', commentcount=666)


# 数据删除 物理删除和逻辑删除
# 方法一
book = BookInfo.objects.get(id=6)
book.delete()


# 方法二

BookInfo.objects.get(id=5).delete()
BookInfo.objects.filter(id=5).delete()


