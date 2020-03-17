# -*- coding=utf-8 -*-
__author__ = 'Shylock'
__time__ = '2020/03/15'

import requests
import pytest
from WeiChat.contract import token
import time
import logging


class Test_user(object):
    logging.basicConfig(level=logging.DEBUG)

    def test_new_user(self):
        uid = str(time.time()).split(".")[0]
        print(uid)
        data = {
    "userid": "zhangsan",
    "name": "张三",
    "alias": "jackzhang",
    "mobile": "13800000000",
    "department": [1, 2],
    "order":[10,40],
    "position": "产品经理",
    "gender": "1",
    "email": "zhangsan@gzdev.com",
    "is_leader_in_dept": [1, 0],
    "enable":1,
    "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
    "telephone": "020-123456",
    "address": "广州市海珠区新港中路",
    "extattr": {
        "attrs": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "网页名称",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            }
        ]
    },
    "to_invite": true,
    "external_position": "高级产品经理",
    "external_profile": {
        "external_corp_name": "企业简称",
        "external_attr": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "网页名称",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            },
            {
                "type": 2,
                "name": "测试app",
                "miniprogram": {
                    "appid": "wx8bd8012614784fake",
                    "pagepath": "/index",
                    "title": "my miniprogram"
                }
            }
        ]
    }
}

        # data = {
        #     "userid": uid,
        #     "name": "12323",
        #     "department": 1
        # }
        re = requests.request("post", "https://qyapi.weixin.qq.com/cgi-bin/user/create",
                              # proxies={"http": "http://127.0.0.1:8877",
                              #          "https": "https://127.0.0.1:8877"},
                              params={"access_token": token.Token.get_token()},
                              data=data
                              ).json()
        print(re)
