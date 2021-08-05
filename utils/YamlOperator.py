from utils.FileOperator import FileOperator
import yaml


class YamlOperator(object):
    @staticmethod
    def readYaml(fileDir, fileName):
        '''
        读取yaml 文件内容
        :param fileDir:
        :param fileName:
        :return:
        '''
        filePath = FileOperator.getFilePath(fileDir, fileName)
        with open(filePath, 'r', encoding='utf-8') as f:
            return list(yaml.safe_load_all(f))
