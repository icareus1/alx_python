"""
    Fetches the content of the URL 'https://alu-intranet.hbtn.io/status'
    using the requests package and displays the body response.
"""


import requests

if __name__ == "__main__":
    res = requests.get('https://alu-intranet.hbtn.io/status')
    content = res.text
    
    print('Body response:')
    print('\t- type:', type(content))
    print('\t- content:', content)