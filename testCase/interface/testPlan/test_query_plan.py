import unittest

from src.interface.api.batchApi import BatchApi
from src.interface.api.loginApi import LoginClient
from src.interface.api.teamApi import TeamApi
from src.interface.api.testPlanApi import TestPlanApi
from src.interface.common.log_decorator import LogDecorator
from src.interface.enum.customEnum import TeamType, Gender


class TestPlan(unittest.TestCase):
    def setUp(self):
        self.token = LoginClient().loginSuccess()  # 登录获取token
        self.client = TestPlanApi()

    @LogDecorator()
    def test_query_plan(self):
        """查询测试计划"""
        team_type = TeamType.NATIONAL_TEAM.value  # 队伍类型为国家队的编号
        team_id = TeamApi().setTeamType(team_type).queryTeam(self.token).getTeamId('男子冰球')  # 获取高山滑雪队的id
        gender = Gender.UNLIMITED.value  # 性别不限
        batch_code = BatchApi().queryBatch(self.token).getKey('大比武')  # 获取正式测试批次编号
        dic = {'teamType': team_type, 'teamId': team_id, 'gender': gender, 'batchCode': batch_code}

        self.client.setProperty(dic)
        plan = self.client.queryPlan(token=self.token)
        sub_set = set(dic.items())
        plan_set = set(plan.items())
        self.assertTrue(sub_set.issubset(plan_set))
        self.assertEqual(200, self.client.statusCode)
        self.assertEqual(1, self.client.totalPages)
        self.assertEqual(1, self.client.totalRows)


if __name__ == '__main__':
    unittest.main()
