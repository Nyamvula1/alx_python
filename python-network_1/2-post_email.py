import sys
import requests

'''taking the arguments(url) from the system which is at position 1'''
url_to_use = input('Enter url= ') if len(sys.argv) < 2 else sys.argv[1]
email=input('Enter email= ') if len(sys.argv) < 3 else sys.argv[2]
data_to_be_sent={'email':email}

'''posting to the url'''

response=requests.post(url=url_to_use, data=data_to_be_sent)
print(response.text)