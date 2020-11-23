from src.common import configInfo
from src.interface.api.baseApi import BaseApi
from src.interface.api.loginApi import LoginClient
from src.interface.config.urlConfig import DictType
from src.interface.httpBase.httpMethod import MethodEnum


class BatchApi(BaseApi):

    def queryBatch(self, token=None):
        url_query = configInfo.get_url(DictType.batch_query)
        self.setAuthToken(token)
        self.sendRequest(method=MethodEnum.GET, url=url_query)
        return self

    def getBatchInfo(self, name):
        for batch in self.responseBody:
            if batch.get('name') == name:
                return batch

    def getKey(self, name):
        return self.getBatchInfo(name).get('key')


if __name__ == '__main__':
    team_api = BatchApi()
    team_api.queryBatch(token=LoginClient().loginSuccess())
    team_info = team_api.getKey('正式测试')
    print(team_info)
