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
        self.params = None
        self.body = None


class Response:
    def __init__(self):
        self.header = dict()
        self.body = None
        self.status_code = 200



class API:
    def __init__(self):
        self.url = ''
        self.name = ''
        self.details = ''
        self.request = None
        self.response = None


if __name__ == '__main__':
    doc = Doc(name='My API List')

    get_book_by_id = API()
    get_book_by_id.details = 'This is the API is about getting book details by ID'
    get_book_by_id.request.header ={'http-api-key':'nksks.wlekjlk43k3isdslk3'}
    get_book_by_id.request.params = {'id':1,'page':1,'size':200}
    get_book_by_id.response.status_code = 200
    get_book_by_id.response.body = {'flag':1,'response':'kl'}

    doc.add_api(get_book_by_id)








    req = Request()
    req.header = {
        'http-api-key': 'bhslks.skjsjsliepoqwjij3oi3jsjd'
    }
    print(req.header)
