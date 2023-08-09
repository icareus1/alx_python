"""
    Fetches a URL, sends a request to the URL, and displays the value of the
    'X-Request-Id' header in the response.
    The URL is passed as an argument.
    Note:
        The value of the 'X-Request-Id' header is different for each request.
"""


import requests, sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    
    if 'X-Request-Id' in res.headers:
        print(res.headers['X-Request-Id'])
    else:
        print('No "X-Request-Id" found in the response header')