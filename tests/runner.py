import pytest
from utils.FileOperator import FileOperator
'''
TODO 需要集成 jenkins
pytest 运行器，  
'''
if __name__ == '__main__':
    resultFilePath = FileOperator.getFilePath(fileDir='report/result', fileName= '')
    htmlFilePath = FileOperator.getFilePath(fileDir='report/html' , fileName= '')

    # 测试结果展示
    # TODO allure 结果
    pytest.main(["-s", "-v", "test_material.py", "--alluredir", resultFilePath, "--clean-alluredir"])
    import subprocess

    subprocess.call('allure generate %s -o %s --clean' % (resultFilePath, htmlFilePath), shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 %s' % (htmlFilePath), shell=True)

    #TODO 钉钉提醒