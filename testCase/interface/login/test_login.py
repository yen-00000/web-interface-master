import unittest

from src.interface.api.loginApi import LoginClient
from src.interface.common.log_decorator import LogDecorator


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.client = LoginClient()

    @LogDecorator()
    def test_login_success(self):
        """登录成功"""
        self.client.login('admin', '123456')
        self.assertEqual(200, self.client.statusCode)

    @LogDecorator()
    def test_login_error(self):
        """登录失败"""
        self.client.login('admin', '111')
        self.assertEqual(401, self.client.statusCode)

    @LogDecorator()
    def test_login_null(self):
        """参数为空"""
        self.client.login()
        self.assertEqual(400, self.client.statusCode)


if __name__ == '__main__':
    unittest.main()
