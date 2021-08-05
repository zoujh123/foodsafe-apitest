from utils.YamlOperator import YamlOperator

'''
获取当前配置信息
'''
class ConfigOperator(object):
    @staticmethod
    def getConfig():
        filePath = 'config'
        fileName = 'config.yaml'
        return YamlOperator.readYaml(filePath, fileName)

    def getLoginInfo(role):
        filePath = 'data'
        fileName = 'login.yaml'
        loginInfo = YamlOperator.readYaml(filePath, fileName)
        return loginInfo[0]['role_' + role]

if __name__ == '__main__':
    '''
    获取当前测试的地址URL 
    '''
    print( ConfigOperator.getLoginInfo('store')['password'])