import requests
from simplejson import JSONDecodeError

from src.common.configInfo import HttpConfig
from src.common.log import logger
from src.interface.httpBase.httpMethod import MethodEnum


class HttpSendBase:

    def __init__(self):
        self.__method = None
        self.__requestUrl = None
        self.__requestBody = {}
        self.__requestHeaders = {}
        self.__timeout = HttpConfig.timeout
        self.__response = None

    def sendRequest(self, method=MethodEnum.GET, url=None):
        self.method = method
        self.requestUrl = url
        requestHeaders = self.getHeader()
        requestBody = self.requestBody
        if method == MethodEnum.POST:
            self.__response = requests.post(url=url, data=requestBody, headers=requestHeaders, timeout=self.timeout)
        elif method == MethodEnum.GET:
            self.__response = requests.get(url=url, params=requestBody, headers=requestHeaders, timeout=self.timeout)
        elif method == MethodEnum.PUT:
            self.__response = requests.put(url=url, data=requestBody, headers=requestHeaders, timeout=self.timeout)
        elif method == MethodEnum.DELETE:
            self.__response = requests.delete(url=url, data=requestBody, headers=requestHeaders, timeout=self.timeout)

        msg = '发送{}请求：{}, headers:{}, data:{}, 响应码:{}, 响应body:{}'.format(method.value, url, requestHeaders, requestBody,
                                                                         self.statusCode, self.responseBody)
        logger.info(msg)
        print(msg)

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        self.__timeout = value

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        if isinstance(value, MethodEnum):
            self.__method = value
        else:
            raise ValueError('method must be a MethodEnum')

    @property
    def requestUrl(self):
        return self.__requestUrl

    @requestUrl.setter
    def requestUrl(self, value):
        self.__requestUrl = value

    def getHeader(self):
        return self.__requestHeaders

    def setHeaders(self, **kwargs):
        self.__requestHeaders.update(kwargs)

    @property
    def requestBody(self):
        return self.__requestBody

    @requestBody.setter
    def requestBody(self, body):
        self.__requestBody = body

    def setProperty(self, dic={}, **kwargs):
        self.requestBody.update(dic)
        for key, value in kwargs.items():
            if value is not None:
                self.requestBody[key] = value
        return self

    @property
    def response(self):
        return self.__response

    @property
    def statusCode(self):
        return self.response.status_code

    @property
    def responseBody(self):
        try:
            return self.response.json()
        except JSONDecodeError as e:
            logger.warning(e)
            return self.response.text
