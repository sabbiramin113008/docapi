# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import codecs
import datetime
import json


class Doc:
    def __init__(self, name):
        self.name = name
        self.base_url = 'http://127.0.0.1:1034'
        self.today = datetime.datetime.now().strftime('%Y %d %b, %I:%M %p')
        self.output_md_file_name = 'document.md'

        self.apis = list()

    def add_api(self, api):
        return self.apis.append(api)

    def build(self):
        components = list()

        components.append('# {}'.format(self.name))
        components.append('`Base URL` - {}\n'.format(self.base_url))

        components.append('`Last Edited` - {}'.format(self.today))

        for indx, api in enumerate(self.apis):
            components.append('## {}. {}'.format(indx + 1, api.name))
            components.append('- {}'.format(api.details))
            components.append('### API Path \n{}{}'.format(self.base_url, api.url))

            components.append('## Request')
            components.append('---------------')

            if len(api.request.method):
                components.append('### Methods')
                components.append('- {}'.format(', '.join([meth.upper() for meth in api.request.method])))

            if api.request.header:
                components.append('### Header')

                Header_val = '```json\n' \
                             '{}\n' \
                             '```'.format(json.dumps(api.request.header, indent=2, ensure_ascii=False))
                components.append(Header_val)
            if api.request.body:
                components.append('### Body')

                Header_val = '```json\n' \
                             '{}\n' \
                             '```'.format(json.dumps(api.request.body, indent=2, ensure_ascii=False))
                components.append(Header_val)

            if api.request.params:
                components.append('### Parameters')
                Param_vals = '```json\n' \
                             '{}\n' \
                             '```'.format(json.dumps(api.request.params, indent=2, ensure_ascii=False))
                components.append(Param_vals)

            components.append('## Response')
            components.append('---------------')

            components.append('`HTTP Status Code` - {}'.format(api.response.status_code))
            if api.response.header:
                components.append('### Header')

                Header_val = '```json\n' \
                             '{}\n' \
                             '```'.format(json.dumps(api.response.header, indent=2, ensure_ascii=False))
                components.append(Header_val)
            if api.response.body:
                components.append('### Body')

                Header_val = '```json\n' \
                             '{}\n' \
                             '```'.format(json.dumps(api.response.body, indent=2, ensure_ascii=False))
                components.append(Header_val)

        complete = '\n'.join(components)
        print(complete)
        with codecs.open(self.output_md_file_name, 'w', 'utf-8') as ff:
            ff.write(complete)

        return complete


class Request:
    def __init__(self, ):
        self.header = {}
        self.params = None
        self.body = None
        self.method = list()


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

    def __repr__(self):
        return 'URL:{}\nName:{}\n,Details:{}\n'.format(self.url, self.name, self.details)

if __name__ == '__main__':
    doc = Doc(name='My API List')

    get_book_by_id = API()
    get_book_by_id.name = 'Get Book By ID'
    get_book_by_id.request.method = ['GET', 'POST']
    get_book_by_id.url = '/api/books/id'
    get_book_by_id.details = 'This is the API is about getting book details by ID'
    get_book_by_id.request.header = {
        'http-api-key': 'nksks.wlekjlk43k3isdslk3'
    }
    get_book_by_id.request.params = {'id': 1, 'page': 1, 'size': 200}
    get_book_by_id.response.status_code = 300
    get_book_by_id.response.body = {'flag': 1, 'response': 'kl'}

    doc.add_api(api=get_book_by_id)

    doc.build()
