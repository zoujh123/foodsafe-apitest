import requests
"""
请求通用类
"""


class Requests(object):
    def request(self, url, method, **kwargs):
        return requests.request(method, url, **kwargs)

    def get(self, url, params = None):
        return requests.get(url=url, params=params)

    def post(self, url, data = None, json = None):
        return requests.post(url=url, data=data, json=json)

    def delete(self, url, **kwargs):
        return requests.delete(url=url, **kwargs)

    def put(self, url, data = None, **kwargs):
        return requests.put(url=url, data=data, **kwargs)
