# -*- coding=utf-8 -*-
__author__ = 'Shylock'
__time__ = '2020/03/15'

import requests
import yaml
import logging


class Token(object):
    logging.basicConfig(level=logging.DEBUG)
    @classmethod
    def get_token(cls):
        conf = yaml.safe_load(open("../data/data.yaml"))
        cls._token = ''
        r = requests.request("get", "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                             params={"corpid": conf["env"]["corpid"],
                                     "corpsecret": conf["env"]["SECRET"]}
                             ).json()
        return r["access_token"]
