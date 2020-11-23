"""
定义配置类，读取配置文件中的配置信息包括[HTTP][USER][EMAIL][LOG]
"""
from read_config import get_http, get_user, get_email, get_log


class HttpConfig:
    scheme = get_http('scheme')
    ssoUrl = get_http('ssoUrl')
    baseUrl = get_http('baseUrl')
    timeout = float(get_http('timeout'))


class UserConfig:
    username = get_user('username')
    password = get_user('password')


class EmailConfig:
    on_off = get_email('on_off')
    title = get_email('title')
    message = get_email('message')
    password = get_email('password')
    receiver = get_email('receiver')
    server = get_email('server')
    sender = get_email('sender')


class LogConfig:
    file_name = get_log('file_name')
    backup = int(get_log('backup'))
    console_level = get_log('console_level')
    file_level = get_log('file_level')


def get_url(path='', url=HttpConfig.baseUrl):
    new_url = '{}://{}{}'.format(HttpConfig.scheme, url, path)
    return new_url


if __name__ == '__main__':
    print(get_url())
