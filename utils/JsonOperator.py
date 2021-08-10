from utils.FileOperator import FileOperator
import json
import time
import random

class JsonOperator(object):
    @staticmethod
    def readJson(fileDir, fileName):
        '''
        读取yaml 文件内容
        :param fileDir:
        :param fileName:
        :return:
        '''
        filePath = FileOperator.getFilePath(fileDir, fileName)
        with open(filePath, 'r', encoding='utf-8') as f:
            jsonString = f.read()
            return jsonString

    @staticmethod
    def parseRandParam(jsonString):
        nowTimestamp = time.time()
        randStr = "%d%d" %(nowTimestamp,  random.randint(0, 100))
        jsonString = jsonString.replace("{rand}", randStr)
        return jsonString

if __name__ == '__main__':
    JsonOperator.readJson("data/material","add.json")