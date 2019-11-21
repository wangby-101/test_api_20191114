# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 15:15
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : request.py
# @Software: PyCharm

import json
import requests
from Common.Configs import Configs
class Request:
    def __init__(self, method, url, data=None, json=None, cookies=None, headers=None):

        URL = Configs().get('URL', 'url') + url

        try:
            if method == 'get':
                self.res = requests.get(url=URL, params=data, cookies=cookies, headers=headers)
            elif method == 'post':
                self.res = requests.post(url=URL, data=data, json=json, cookies=cookies, headers=headers)
            else:
                self.res = requests.request(method=method, url=URL, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_code(self):
        return self.res.status_code

    def get_text(self):
        return self.res.text

    def get_json(self):
        return self.res.json()

    def get_cookies(self, key=None):
        if key:
            return self.res.cookies
        else:
            return self.res.cookies[key]

if __name__ == '__main__':
    url = "/member/login"
    data = {"mobilephone":"15942123962","pwd":"abc1234"}
    res = Request("get", url=url, data=data)
    print(res.get_text())