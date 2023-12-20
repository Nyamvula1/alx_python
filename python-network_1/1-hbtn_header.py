import sys
import requests

'''taking the arguments(url) from the system which is at position 1'''
url=input('Enter url= ') if len(sys.argv) < 2 else sys.argv[1]
'''the response from the system'''

response=requests.get(url)

'''check whether the x-request-id is in response header''' 
if 'X-Request-Id' in response.headers:
    x= response.headers['X-Request-Id']
    print(x)