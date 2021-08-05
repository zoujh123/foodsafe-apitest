'''
测试物料信息
'''
import pytest
from utils.ExcelOperator import ExcelOperator, ExcelVars
from tests.login import login_success
from utils.Requests import Requests
from utils.ConfigOperator import ConfigOperator
import json
import allure

excel = ExcelOperator(fileName='material.xlsx')
requests = Requests()


# TODO 失败后重跑1次， 间隔2秒，验证是否有效果
@pytest.mark.flaky(reruns=1, reruns_delay=2)
# 参数化
@allure.title("物料设置")
@pytest.mark.parametrize("datas", excel.runs())
def test_material(datas, login_success):
    # 动态设置title
    allure.dynamic.title("物料设置 - " + datas[ExcelVars.caseName])

    # 对请求参数做 反序列化的处理
    params = datas[ExcelVars.params]
    if len(str(params).strip()) == 0:
        pass
    elif len(str(params).strip()) >= 0:
        # TODO 参数需要设置随机变量
        params = json.loads(params)

    # 对请求头做反序列化的处理
    header = datas[ExcelVars.headers]
    if len(str(header).strip()) == 0:
        pass
    elif len(str(header).strip()) >= 0:
        # 设置 JWT 请求头参数
        if '{token}' in header:
            header = header.replace('{token}', login_success)
        header = json.loads(header)

    # 设置地址
    url = ConfigOperator.getConfig()[0]['siteUrl'] + datas[ExcelVars.caseUrl]

    # 设置对应的请求参数
    jsonParams = None
    dataParams = None
    queryParams = None
    if datas[ExcelVars.contentType] == 'json':
        jsonParams = params
    elif datas[ExcelVars.contentType] == 'query':
        queryParams = params
    elif datas[ExcelVars.contentType] == 'form':
        dataParams = params

    result = requests.request(url=url, method=datas[ExcelVars.method], headers=header, json=jsonParams, data=dataParams,
                              params=queryParams)

    # 验证返回的status code
    assert result.status_code == datas[ExcelVars.statusCode]

    # 验证期望的结果是否符合
    # TODO 扩展更灵活的断言方式
    assert datas[ExcelVars.expect] in json.dumps(result.json(), ensure_ascii=False)
