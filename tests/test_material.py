'''
测试物料信息
'''
import pytest
from utils.ExcelOperator import ExcelOperator, ExcelVars
from tests.login import login_success
from utils.ParamOperator import parseRandParam, parseResultParam
from utils.Requests import Requests
from utils.ConfigOperator import ConfigOperator
from utils.JsonOperator import JsonOperator
import json
import re
import allure

excel = ExcelOperator(fileName='material.xlsx')
requests = Requests()
result_params_container = {}

# TODO 失败后重跑1次， 间隔2秒，验证是否有效果
@pytest.mark.flaky(reruns=1, reruns_delay=2)
# 参数化
# @allure.title("物料设置")
@pytest.mark.parametrize("datas", excel.runs())
def test_material(datas, login_success):
    # 动态设置title
    allure.dynamic.title("物料设置 - " + datas[ExcelVars.caseName])

    # 对请求参数做 反序列化的处理
    params = datas[ExcelVars.params]
    if len(str(params).strip()) == 0:
        pass
    elif len(str(params).strip()) >= 0:
        # TODO 参数从 data/material/add.json 中获取, 无需都写在 excel 中， 太冗长
        params = JsonOperator.readJson("data", params)
        # TODO 替换随机变量
        params = parseRandParam(params)
        # TODO 设置上一次获取的结果，替换掉这个变量，执行下一次的结果
        params = parseResultParam(result_params_container, params)
        # 转JSON
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
    url = parseResultParam(result_params_container, url)

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

    jsonData = result.json()

    # 解析方法
    result_parse = datas[ExcelVars.resultParse]
    if len(str(result_parse).strip()) > 0:
       print(result_parse)
       # 渲染后的结果
       parse_arr =  result_parse.split(".")
       result_data = None
       for parseParam in parse_arr:
           pattern = re.compile(r'[\d+]')
           idx = pattern.findall(parseParam)
           if len(idx) > 0:
               parseParam = (int)(idx[0])
           if result_data == None:
               result_data = jsonData[parseParam]
           else:
               result_data = result_data[parseParam]


       # 保存结果参数
       result_param = datas[ExcelVars.resultParam]
       if len(str(result_parse).strip()) >= 0:
           result_params_container[result_param] = result_data


    # 验证返回的status code
    assert result.status_code == datas[ExcelVars.statusCode]

    # 验证期望的结果是否符合
    # TODO 扩展更灵活的断言方式
    assert datas[ExcelVars.expect] in json.dumps(result.json(), ensure_ascii=False)
    # TODO 保存上一次的结果，用于下一次的计算
