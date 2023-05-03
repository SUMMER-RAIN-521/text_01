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
    # request, 请求 template_name, 模板名称
    # context = None, content_type = None,
    # status = None, using = None

    # 模拟数据查询
    context = {
        'name': '马上双11,点击有惊醒！'
    }
    return render(request, 'book/index.html', context=context)







