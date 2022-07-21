import pytest
from utils.FileOperator import FileOperator
from utils.senddingtalk import SendDingtalk

'''
TODO 需要集成 jenkins
pytest 运行器，  
'''
if __name__ == '__main__':
    resultFilePath = FileOperator.getFilePath(fileDir='report/result', fileName='')
    htmlFilePath = FileOperator.getFilePath(fileDir='report/html', fileName='')

    # 测试结果展示
    # TODO allure 结果
    res = pytest.main(["-s", "-v", "test_material_unit.py", "--alluredir", resultFilePath, "--clean-alluredir"])

    # TODO 获取报告的结果
    content = "测试环境：%s.测试结果: 通过[%s]，失败[%s],错误[%s],跳过[%s]" % ( "食安测试环境" , "1","2","3","4")

    # 通过邮件，钉钉发送测试报告结果链接
    sendDingtalk = SendDingtalk()
    message_url = "http://192.168.0.217:8088"
    report_title = u"食安2.0测试报告结果"
    sendDingtalk.post_link(content, report_title, "", message_url)

    import subprocess
    subprocess.call('allure generate %s -o %s --clean' % (resultFilePath, htmlFilePath), shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 %s' % (htmlFilePath), shell=True)
