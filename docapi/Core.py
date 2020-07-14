# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 25 Jun 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import datetime


class Doc:
    def __init__(self, name):
        self.name = name
        self.today = datetime.datetime.now().strftime('%Y_%d%b_%I_%M_%p')
        print(self.today)
        self.apis = list()

    def add_api(self, api):
        return self.apis.append(api)

    def build(self):
        pass


class Request:
    def __init__(self, ):
        self.header = {}
        self.body = None


class Response:
    def __init__(self):
        self.header = dict()
        self.body = None
        self.status_code = 200



class API:
    def __init__(self, url, name, details, request, response):
        self.url = url
        self.name = name
        self.details = ''
        self.request = request
        self.response = response


if __name__ == '__main__':
    doc = Doc(name='My API List')

    req = Request()
    req.header = {
        'http-api-key': 'bhslks.skjsjsliepoqwjij3oi3jsjd'
    }
    print(req.header)
