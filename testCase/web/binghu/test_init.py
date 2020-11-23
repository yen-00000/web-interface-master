"""
初始化用例，用来验证init.yaml脚本是否能成功登陆
"""
import unittest

from src.web.common.YamlHandler import YamlHandler


class TestInit(unittest.TestCase):
    def test(self):
        result = YamlHandler().run(yaml_name='init')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()




