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
        self.base_url = 'someid:'
        self.today = datetime.datetime.now().strftime('%Y_%d%b_%I_%M_%p')
        print(self.today)
        self.apis = list()

    def add_api(self, api):
        return self.apis.append(api)

    def build(self):
        api_list = list()
        for api in self.apis:
            api_name = '## {}'.format(api.name)
            api_details = '{}'.format(api.details)
            div1  = '---------------'
            url = '###\'URL\'\n{}{}'.format(self.base_url, api.url)

            Req = '## Request'
            div2 = '---------------'

            Header_key= '### Header'
            Header_val = '```json' \
                         '{}' \
                         '```'.format(api.request.header)
            Param_key = '### Parameters'
            Param_vals = '```json' \
                         '{}' \
                         '```'.format(api.request.params)
            complete = '\n'.join([api_name,api_details,div1,url,Req,div2,Header_key,
                                  Header_val,Param_key,Param_vals])
            print (complete)


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
        self.request = Request()
        self.response = Response()


if __name__ == '__main__':
    doc = Doc(name='My API List')


    get_book_by_id = API()
    get_book_by_id.url = '/api/books/id'
    get_book_by_id.details = 'This is the API is about getting book details by ID'
    get_book_by_id.request.header ={'http-api-key':'nksks.wlekjlk43k3isdslk3'}
    get_book_by_id.request.params = {'id':1,'page':1,'size':200}
    get_book_by_id.response.status_code = 200
    get_book_by_id.response.body = {'flag':1,'response':'kl'}

    doc.add_api(get_book_by_id)

    doc.build()
