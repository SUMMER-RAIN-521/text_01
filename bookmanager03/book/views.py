from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import BookInfo

# Create your views here.



def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2001-9-4',
        readcount=10
    )
    return HttpResponse('create')


'''
url以？分割为两部分，后面一部分为查询字符串，多个数据以&拼接
查询字符串类似于字典
'''
def shop(request, city_id, mobile):

    query_params = request.GET
    print(query_params)
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
    return HttpResponse('method')


from django.http import JsonResponse


def res(request):
    # HTTP status code must be an integer from 100 to 599.
    # response = HttpResponse('res')
    # response['name']='xiayuxuan'

    # json-->dict
    # dict-->json
    info = {
        "name": "itcast",
        "address": "shunyi"
    }
    girl_firends=[
        {
            "name": "kunkun",
            "address": "loudi"
        },
        {
            "name": "siri",
            "address": "changsha"
        }
    ]
    # data 返回响应数据 一般是字典类型
    """
    safe =True 表示的data是字典数据
    JsonResponse 可以把字典转换为json
    """
    # response = JsonResponse(data=girl_firends, safe=False)
    # return response
    # 重定向
    return redirect("http://www.baidu.com")


# Cookie和Session
'''
第一次请求携带查询字符串
127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器接受到请求后，提取username,服务器设置cookie信息，信息包括username
浏览器接受到响应后把cookie信息保存起来
第二次及其之后的请求访问127.0.0.1:8000/set_cookie/?username=itcast&password=123
都会携带cookie信息，服务器根据cookie信息判断用户身份
'''


def set_cookie(request):
    # 1.获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2.服务器设置cookie信息，通过响应对象.set_cookie的方法
    response = HttpResponse('set_cookie')
    # key, value=''
    response.set_cookie('name', username, max_age=60*60)
    response.set_cookie('pwd', password)
    # 删除cookie
    # response.delete_cookie('name')
    return response


def get_cookie(request):
    print(request.COOKIES)  # 字典数据
    return HttpResponse(request.COOKIES.get('pwd'))

# session 是保存在服务器的，数据相对安全
# session 需要依赖于cookie

'''
第一次请求 网站 服务器端会设置session信息
服务器同时产生一个session_id 的cookie信息
浏览器受到这个信息后会把cookie保存起来

第二次都会携带session_id信息，服务器验证信息，没有问题则会读取相关信息
'''

def set_session(request):
    # 1.模拟准备用户信息
    username = request.GET.get('username')
    # 2. 设置session信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    # clear 删除session里面的数据，但是key有所保留
    # request.session.clear()
    # flush 删除session的所有数据
    # request.session.flush()

    # 设置国旗时间
    request.session.set_expiry(3600)
    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    content = "{}, {}".format(user_id, username)
    return HttpResponse(content)






