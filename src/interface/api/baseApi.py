from src.interface.httpBase.httpSendBase import HttpSendBase


class BaseApi(HttpSendBase):
    def __init__(self):
        super().__init__()
        self.__code = None
        self.__msg = None
        self.setContentType()

    @property
    def code(self):
        return self.responseBody.get('code')

    @property
    def msg(self):
        return self.responseBody.get('msg')

    @property
    def data(self):
        return self.responseBody.get('data')

    @property
    def totalRows(self):
        return self.responseBody.get('totalRows')

    @property
    def totalPages(self):
        return self.responseBody.get('totalPages')

    @property
    def currentPage(self):
        return self.responseBody.get('currentPage')

    @property
    def pageRows(self):
        return self.responseBody.get('pageRows')

    def setAuthToken(self, bearToken):
        if bearToken is not None:
            self.setHeaders(Authorization=bearToken)

    def setContentType(self, content_type='application/json;charset=UTF-8'):
        self.setHeaders(Content_Type=content_type)
