from django.urls import path

from book.views import create_book, shop, register, json, method

urlpatterns = [
    path('create/', create_book),
    # <转换器的名字：变量名> 转换器会对变量名进行正则验证
    path('<int:city_id>/<int:shop_id>', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method)
]