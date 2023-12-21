import sys
import requests

url = input('Enter url= ') if len(sys.argv) < 2 else sys.argv[1]
response=requests.get(url)
if response.status_code >= 400:
    print('Error code:{}'.format(response.status_code))
else: 
    print(response.text)
