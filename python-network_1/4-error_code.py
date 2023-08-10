"""
    Fetches a URL, sends a request to the URL, and displays the body of the
    response. Prints an error message if the HTTP status code is >= 400.
"""



import requests
import sys

if __name__ == "__main__":
    res = request.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)