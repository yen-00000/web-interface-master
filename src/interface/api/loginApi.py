from src.interface.httpBase.httpMethod import MethodEnum

from src.common.configInfo import get_url, UserConfig, HttpConfig
from src.interface.api.baseApi import BaseApi
from src.interface.common import endecrypt
from src.interface.config.urlConfig import LoginUrl


class LoginClient(BaseApi):

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__pwd = None

    def login(self, name=None, pwd=None):
        url_login = get_url(LoginUrl.login, HttpConfig.ssoUrl)
        self.name = name
        self.pwd = pwd
        self.setProperty(grant_type='password')
        self.setAuthToken('Basic NzlpWjBOOWM2UWM2a0FuYzRKNVNmYzM5OkkxTkFxVGVlYzROS1k0NmNpVHBNeFlCMA==')
        self.setContentType('application/x-www-form-urlencoded')
        self.setHeaders(
            Cookie='experimentation_subject_id=Ijg5ZWVjZDRkLTRlZjMtNGMzYy1iYzE2LWJlYjVjYzk5OWYyOSI%3D'
                   '--e1502bffe01497922b1c41dc7e9058da282fef49')
        self.sendRequest(method=MethodEnum.POST, url=url_login)

    def loginSuccess(self):
        self.login(UserConfig.username, UserConfig.password)
        return self.bearToken

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.setProperty(username=self.__name)

    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, value):
        self.__pwd = value if value is None else endecrypt.encrypt_md5(value)
        self.setProperty(password=self.__pwd)

    @property
    def token(self):
        return self.responseBody.get('access_token')

    @property
    def bearToken(self):
        return 'Bearer ' + self.token


if __name__ == '__main__':
    loginClient = LoginClient()
    loginClient.login()
    loginClient.loginSuccess()
