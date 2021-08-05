import os


class FileOperator(object):
    @staticmethod
    def getFilePath(fileDir='data', fileName='login.yaml'):
        '''
        获取文件的目录（从 根目录开始）
        :param fileDir: 文件的目录
        :param fileName: 文件的名称
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)

    @staticmethod
    def writeContent(fileDir, fileName, content):
        '''
        写入文件
        :param fileDir: 文件的目录
        :param fileName: 文件的名称
        :param content: 写入的内容
        :return:
        '''
        filePath = FileOperator.getFilePath(fileDir, fileName)
        with open(filePath, 'w') as f:
            f.write(content)

    @staticmethod
    def readContent(fileDir, fileName):
        '''
        读取文件内容
        :param fileDir: 文件的目录
        :param fileName: 文件的名称
        :return:
        '''
        filePath = FileOperator.getFilePath(fileDir, fileName)
        with open(filePath, 'r') as f:
            return f.read()
