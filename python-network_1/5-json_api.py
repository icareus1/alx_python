"""
    Sends a POST request to http://0.0.0.0:5000/search_user with a letter as
    a parameter and displays the response based on the conditions.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    
    url = 'http://0.0.0.0:5000/search_user'
    load = {'q': q}
    
    res = requests.post(url, data=load)
    
    try:
        data = res.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
