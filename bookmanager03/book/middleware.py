from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print('1111111111每次请求都会执行')
        username = request.COOKIES.get('username')
        if username is None:
            print('没有用户信息')
        else:
            print("有用户信息")

    def process_response(self, request, response):
        print('每次响应前，都会执行111111111111')
        return response


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print('222222222每次请求都会执行')
        username = request.COOKIES.get('username')
        if username is None:
            print('没有用户信息')
        else:
            print("有用户信息")


    def process_response(self, request, response):
        print('每次响应前，都会执行2222222222')
        return response


