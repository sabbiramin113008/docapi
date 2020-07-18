# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 19 Jul 2020
email:  sabbiramin.cse11ruet@gmail.com

"""
from docapi import Doc, API

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
