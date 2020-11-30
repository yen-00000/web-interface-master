from src.api.baseApi import BaseApi


class TestGen(BaseApi):
	def __init__(self):
		super().__init__()
		self.__code = None
		self.__msg = None
		pass

	@property
	def code(self):
		return self.__code

	@code.setter
	def code(self, value):
		self.__code = value

	@property
	def msg(self):
		return self.__msg

	@msg.setter
	def msg(self, value):
		self.__msg = value

	def toDict(self):
		dict1 = {
			'code': self.__code,
			'msg': self.__msg,
			}
		return dict1
	pass
