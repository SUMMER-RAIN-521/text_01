from django.shortcuts import render

# Create your views here.
"""
视图
其实就是python函数
1.视图的第一个参数就是接受请求，这个请求就是HttpRequest的类对象
2.必须返回一个响应

"""
from django.http import HttpRequest
from django.http import HttpResponse

# 我们期望用户输入http://127.0.0.1:8000/index/
# 来访问视图函数


def index(request):
    return HttpResponse('hello!')







