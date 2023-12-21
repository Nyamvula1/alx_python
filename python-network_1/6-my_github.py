import requests
import sys

url="https://api.github.com/user"
username=input('Enter your username: ') if len(sys.argv) < 2 else sys.argv[1]
password=input('Enter your password: ') if len(sys.argv) < 3 else sys.argv[2]

response = requests.get(url=url, auth=(username, password))

if response.status_code == 200:
    user_id= response.json()['id']
    print(user_id)
else:
    print('None')

