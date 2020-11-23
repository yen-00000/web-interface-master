from src.common import configInfo
from src.interface.api.baseApi import BaseApi
from src.interface.api.loginApi import LoginClient
from src.interface.config.urlConfig import TeamUrl
from src.interface.enum.customEnum import TeamType
from src.interface.httpBase.httpMethod import MethodEnum


class TeamApi(BaseApi):

    def queryTeam(self, token=None):
        url_query = configInfo.get_url(TeamUrl.team_query)
        self.setAuthToken(token)
        self.sendRequest(method=MethodEnum.GET, url=url_query)
        return self

    def setTeamType(self, team_type):
        return self.setProperty(teamType=team_type)

    def getTeamInfo(self, teamName):
        for team in self.responseBody:
            if team.get('teamName') == teamName:
                return team

    def getTeamId(self, teamName):
        return self.getTeamInfo(teamName).get('id')


if __name__ == '__main__':
    team_api = TeamApi().setTeamType(TeamType.NATIONAL_TEAM.value)
    team_api.queryTeam(token=LoginClient().loginSuccess())
    team_info = team_api.getTeamId('高山滑雪')
    print(team_info)
