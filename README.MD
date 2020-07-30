## Intro

`docapi` is a Python API Documentation Utility.
Write API documentation as you write codes and Generate Mock Server Code Immediately.
   
## Why Build Another One, When We Already Have So Many?
1. It is always fun to learn something while building it.
2. I wanted to build simple, yet expressive tool that makes writing 
API documentation fun, expressive, engaging and distinctive.
3. I love to create, mimic and explore.

## How to Install `docapi`
---------------------------

## Using Pip
```python
pip install git+https://github.com/sabbiramin113008/docapi.git

```
## How to Prepare the API Documentation
Writing documentation involves 4 entities.
- Doc
- API
- Request and 
- Response

First, create a `Doc` object. 

```python
doc = Doc(name='My Demo API List')
```

You can set Base URL of your APIs,
```python
doc.base_url = 'http://127.0.0.1:8088'
```
or can leave it default to `http://127.0.0.1:1034`

Now time to work with `API` entity.

An `API` object can be consist of these following properties, while instantiation.

But first, instantiate an API object.
```python
get_book_details_by_id = API()
```

Now, you can set `name`, `details` and `url` straight to this API.
```python
...
get_book_details_by_id.name = 'Get Book Details By ID'
get_book_details_by_id.url = '/api/books/id'
get_book_details_by_id.details = 'Some Dummy Details'
```

Now, lets set the Request and Response to this api.

Setting `http method` name, `request header` is simple. Try like this,
```python
...
get_book_details_by_id.request.method = ['GET']
get_book_details_by_id.request.header = {
    'http-api-key':'amkik.skskjuweoiwreoiudf'
}
```
`URL params` can also be set in the same manner. Just add a python dictionary.
```python
...
get_book_details_by_id.request.params = {
    'isActive':1,
    'sortBy':'Date',
    'page':1,
    'size':200
}
```
A `request body` can also be set, like
```python
...
get_book_details_by_id.request.body = {
    'name':'John Doe',
    'occupation':'Developer'
}
```

Now let's process the Response entity of the API.

Add `Response body`, `HTTP Status Code` and `Response Header` Like this,
```python
...
get_book_details_by_id.response.header = {
    'http-api-key':'kdkkd.kdkkddkdkdddldl'
}
get_book_details_by_id.response.status_code = 200
get_book_details_by_id.response.body = {
    'id':'1',
    'name':'John Doe',
    'hasDelivered':True
}
```

Now, we have to `register` this `api` to our `doc object`. Let's

```python
...
doc.add_api(get_book_details_by_id)
```
After registering all the APIs to the doc, we simply generate the file with all the API documentation, 
simply by this command, 
```python
doc.build()
```
A 'document.md' will be generated afterwards. 

## How To Build a Mock API Server
----------------------------------

The lates version of this module can generate simple `Flask` based Web Application
Server, from the documentation. Just add,
```python
...
doc.build_server()
```
This will generate a `server.py` file with all the API routes. 

Detailed Example can be found on the `Example` directory.

'NB' The Server code is written using `Flask`, so it is necessary to have this installed on your machine, 
if you are willing to generate the server code for your mock service.


Voila, it is easy, simple and expressive.