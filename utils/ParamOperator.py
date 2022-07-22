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
    # nowTimestamp = time.time()
    randStr = "%d" % (random.randint(0, 1000))
    jsonString = jsonString.replace("{rand}", randStr)
    return jsonString

def parseRandParamChinese(jsonString):
    # nowTimestamp = time.time()
    randStr = random.randint(0x4e00, 0x9fbf)
    jsonString = jsonString.replace("{rand}", chr(randStr))
    return jsonString

