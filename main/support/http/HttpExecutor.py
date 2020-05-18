import requests

from main.interface.test.TestInterface import TestInterface


class HttpExecutor:

    @staticmethod
    def executor(http_request):
        param = http_request.getParam()
        uri = http_request.getUri()
        method = http_request.getMethod()
        response = None
        if method == 'get':
            response = requests.get(uri, params=param)
        elif method == 'post':
            response = requests.post(uri, data=param)

        return response.json()



