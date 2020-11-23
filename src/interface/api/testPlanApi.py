from src.common import configInfo
from src.interface.api.baseApi import BaseApi
from src.interface.api.loginApi import LoginClient
from src.interface.config.urlConfig import PlanUrl
from src.interface.httpBase.httpMethod import MethodEnum


class TestPlanApi(BaseApi):

    def queryPlan(self, page=1, row=10, token=None):
        url_query = configInfo.get_url(PlanUrl.plan_page)
        self.setProperty(page=page, row=row)
        self.setAuthToken(token)
        self.sendRequest(method=MethodEnum.GET, url=url_query)
        return self.planInfo

    @property
    def planInfo(self):
        return self.data[0]


if __name__ == '__main__':
    info = TestPlanApi().queryPlan(token=LoginClient().loginSuccess())
    print(info)
