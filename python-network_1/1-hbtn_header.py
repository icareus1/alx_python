


import requests, sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    
    if 'X-Request-Id' in res.headers:
        print(res.headers['X-Request-Id'])
    else:
        print('No "X-Request-Id" found in the response header')