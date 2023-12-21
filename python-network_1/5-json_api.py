import sys
import requests

url= 'http://0.0.0.0:5000/search_user'
'''this condition checks for the lenght of the arguments in the command line , if the length is 1 then it returns an empty string'''
q =''if len(sys.argv) == 1 else sys.argv[1]
'''payload-the letter is sent to the server in the format of a dictionary in the payload'''
payload = {'our_letter': q}
response= requests.post(url=url, data=payload)

try:
    if not response.json():
        print('No result')
    else:
        id = response.json().get('id')
        name = response.json().get('name')
        print(f'[{id}] {name}')
except ValueError:
    print('Not a valid JSON')

