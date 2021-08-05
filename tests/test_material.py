'''
测试物料信息
'''
import pytest
from utils.ExcelOperator import ExcelOperator, ExcelVars
from tests.login import login_success
from utils.Requests import Requests
from utils.ConfigOperator import ConfigOperator
import json

excel = ExcelOperator(fileName='material.xlsx')
requests = Requests()

@pytest.mark.parametrize("datas", excel.runs())
def test_material(datas, login_success):
    # 对请求参数做 反序列化的处理
    params = datas[ExcelVars.params]
    if len(str(params).strip()) == 0:
        pass
    elif len(str(params).strip()) >= 0:
        params = json.loads(params)

    # 对请求头做反序列化的处理
    header = datas[ExcelVars.headers]
    if len(str(header).strip()) == 0:
        pass
    elif len(str(header).strip()) >= 0:
        if '{token}' in header:
            header = header.replace('{token}', login_success)
        header = json.loads(header)

    url = ConfigOperator.getConfig()[0]['siteUrl'] + datas[ExcelVars.caseUrl]
    jsonParams = None
    dataParams = None
    queryParams = None
    if datas[ExcelVars.contentType] == 'json':
        jsonParams = params
    elif datas[ExcelVars.contentType] == 'query':
        queryParams = params
    elif datas[ExcelVars.contentType] == 'form':
        dataParams = params

    result = requests.request(url=url, method=datas[ExcelVars.method], headers=header,json = jsonParams, data = dataParams, params = queryParams)
    assert result.status_code == datas[ExcelVars.statusCode]
    assert datas[ExcelVars.expect] in json.dumps(result.json(), ensure_ascii=False)


if __name__ == '__main__':
    print("begin test")
    ## 测试结果展示
    pytest.main(["-s", "-v", "test_material.py", "--alluredir", "./report/result"])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html', shell=True)
