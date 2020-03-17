# -*- coding=utf-8 -*-
__author__ = 'Shylock'
__time__ = '2020/03/16'

from WeiChat.contract import token


class Test_token():
    def test1(self):
        token.Token.get_token()