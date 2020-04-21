
'''。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。有错误。。。。。。。。。。。。。。。。。。。。。。。'''

from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def __init__(self, request):
        print('__init__')

    def process_request(self, request):
        print('process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('process_view')

    def process_response(self, request, response):
        print('process_response')
        return response

    def process_exception(self, request, exception):
        print(exception)