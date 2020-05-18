# http请求的信息
import abc


class HttpRequest(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getMethod(self): pass

    @abc.abstractmethod
    def getUri(self): pass

    @abc.abstractmethod
    def getParam(self): pass
