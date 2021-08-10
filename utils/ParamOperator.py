"""
参数替换
"""
import random
import time


def parseResultParam(map, params):
    for key in map:
        params = params.replace("{%s}" % key, str(map[key]))
    return params


"""
随机数
"""
def parseRandParam(jsonString):
    nowTimestamp = time.time()
    randStr = "%d%d" % (nowTimestamp, random.randint(0, 100))
    jsonString = jsonString.replace("{rand}", randStr)
    return jsonString
