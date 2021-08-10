
import requests
import json
import time
from utils.ConfigOperator import ConfigOperator

class SendDingtalk(object):
    '''
    钉钉配置信息
    '''
    def __init__(self):
        self._access_token =   ConfigOperator.getConfig()[0]['dingtalk_access_token']
        self._tag =  ConfigOperator.getConfig()[0]['dingtalk_tags']
        self.api_url = "https://oapi.dingtalk.com/robot/send?access_token=" + self._access_token

    def post_text(self, text):
        text = self._tag + text
        headers = {'Content-Type': 'application/json;charset=utf-8'}

        data = {}
        data["msgtype"] = "text"
        data["text"] = {}
        data["text"]["content"] = text
        data = json.dumps(data)

        try:
            res = requests.post(self.api_url, data, headers=headers).content
            print(res)
            time.sleep(1)

        except Exception as e:
            print(e)

    def post_link(self, text, title, picurl="", messageurl=""):

        data = {}
        data["msgtype"] = "link"
        data["link"] = {}
        data["link"]["text"] = self._tag + text
        data["link"]["title"] = title
        data["link"]["picUrl"] = picurl
        data["link"]["messageUrl"] = messageurl
        data = json.dumps(data)

        headers = {'Content-Type': 'application/json;charset=utf-8'}
        try:
            res = requests.post(self.api_url, data, headers=headers).content
            print(res)
            time.sleep(1)

        except Exception as e:
            print(e)


if __name__ == '__main__':

    sendDingtalk = SendDingtalk()
    sendDingtalk.post_text('dingtalk')