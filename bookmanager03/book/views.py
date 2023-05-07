from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo

# Create your views here.


# url以？分割为两部分，后面一部分为查询字符串，多个数据以&拼接
def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2001-9-4',
        readcount=10
    )
    return HttpResponse('create')


def shop(request, city_id, mobile):

    query_params = request.GET
    # print(query_params)
    oder = query_params.getlist('key')
    print(oder)

    print(city_id, mobile)
    return HttpResponse('起火啦！')


def register(request):

    data = request.POST
    print(data)

    return HttpResponse('ok')


def json(request):
    body = request.body
    body_str = body.decode()
    print(body_str) # 字符串
    print(type(body_str))
    # json的字符串可以转换为python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    # 请求头的数据
    # print(request.META)
    print(request.META['SERVER_PORT'])
    return HttpResponse('json')


def method(request):

    print(request.method)
    return  HttpResponse('method')









