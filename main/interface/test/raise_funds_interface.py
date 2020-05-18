from main.support.http.HttpRequest import HttpRequest


# http请求
class RaiseFundsInterface(HttpRequest):
    def getMethod(self):
        return 'post'

    def getUri(self):
        return 'https://localhost:9393/mjyx-kf/api/v1/after/query/getNow'

    def getParam(self):
        return ''
