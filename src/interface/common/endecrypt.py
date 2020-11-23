from hashlib import md5


def encrypt_md5(str_data):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(str_data.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


if __name__ == '__main__':
    print(encrypt_md5('123456'))
