"""
    Sends a POST request to a URL with an email as a parameter and displays
    the body of the response.
"""



import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    load = {'email': email}
    
    res = requests.post(url, data=load)
    
    print(res.text)