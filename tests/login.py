import pytest

from utils.ConfigOperator import ConfigOperator
from utils.Requests import Requests

requests = Requests()


@pytest.fixture(scope="session")
def login_success():
    role = 'store'
    print('角色类型是' + role)
    loginUserName = ConfigOperator.getLoginInfo(role)['username']
    loginPassword = ConfigOperator.getLoginInfo(role)['password']
    siteUrl = ConfigOperator.getConfig()[0]['siteUrl']
    loginUrl = ConfigOperator.getConfig()[0]['loginUrl']
    logoutUrl = ConfigOperator.getConfig()[0]['logoutUrl']
    print(siteUrl + loginUrl)
    data = requests.post(url=siteUrl + loginUrl, data={
        'username': loginUserName,
        'password': loginPassword,
        'endpoint': 'pc'
    })
    assert data.status_code == 200
    # 返回 bear token
    jwt = data.json()['value']
    yield jwt

    ## 退出登陆
    header = {
        "Authorization": "Bearer " + jwt
    }
    res = requests.request(url=siteUrl + logoutUrl, method="get", headers=header)
    assert res.status_code == 200
