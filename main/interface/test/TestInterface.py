from main.support.http.HttpRequest import HttpRequest


# http请求
class TestInterface(HttpRequest):
    def getMethod(self):
        return 'get'

    def getUri(self):
        return 'http://localhost:9393/mjyx-kf/api/v1/after/query/getNow'

    def getParam(self):
        return ''
