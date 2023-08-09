"""
    Uses Basic Authentication with a personal access
    token to access the GitHub API and display the user ID.
"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    
    url = 'https://api.github.com/user'
    headers = {'Authorization': 'Basic {}:{}'.format(username, token)}
    
    res = requests.get(url, headers=headers)
    
    try:
        data = res.json()
        print("User ID:", data['id'])
    except ValueError:
        print("Error retrieving user information")
