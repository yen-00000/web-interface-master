import unittest
from src.web.common.BaseYamlTest import BaseTest


class TestCase(BaseTest):
	def test(self):
		result = self.handler.run(yaml_name='delete_athletes')
		self.assertTrue(result)


if __name__ == '__main__':
	unittest.main()
