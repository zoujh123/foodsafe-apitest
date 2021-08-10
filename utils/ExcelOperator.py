import xlrd
import json
from utils.FileOperator import FileOperator

class ExcelVars:
    caseID = "测试用例ID"
    caseModel = "模块"
    caseName = "接口名称"
    caseUrl = "请求地址"
    method = "请求方法"
    paramsType = "请求参数类型"
    params = "请求参数"
    expect = "期望结果"
    isRun = "是否运行"
    headers = "请求头"
    statusCode = "状态码"
    contentType = "请求文本类型"
    resultParse = "保存结果解析方式"
    resultParam = "保存结果变量"


'''
对 EXCEL 进行操作
'''
class ExcelOperator(object):

    def __init__(self,fileDir = 'data', fileName = 'material'):
        self.fileDir = fileDir
        self.fileName = fileName

    def getSheet(self):
        book = xlrd.open_workbook(FileOperator.getFilePath(self.fileDir, self.fileName))
        return book.sheet_by_index(0)

    @property
    def getExcelDatas(self):
        datas = list()
        title = self.getSheet().row_values(0)
        # 忽略首行
        for row in range(1, self.getSheet().nrows):
            row_values = self.getSheet().row_values(row)
            datas.append(dict(zip(title, row_values)))
        return datas


    def runs(self):
        '''获取到可执行的测试用例'''
        run_list = []
        for item in self.getExcelDatas:
            isRun = item[ExcelVars.isRun]
            if isRun == 'y':
                run_list.append(item)
            else:
                pass
        return run_list

    def case_lists(self):
        '''获取excel中所有的测试点'''
        cases = list()
        for item in self.getExcelDatas:
            cases.append(item)
        return cases

    def params(self):
        '''对请求参数为空做处理'''
        params_list = []
        for item in self.runs():
            params = item[ExcelVars.params]
            if len(str(params).strip()) == 0:
                pass
            elif len(str(params).strip()) >= 0:
                params = json.loads(params)