import sys
import requests

url= input('Enter url: ') if len(sys.argv) < 2 else sys.argv[1]
'''this condition checks for the lenght of the arguments in the command line , if the length is 1 then it returns an empty string'''
q =''if len(sys.argv) == 1 else sys.argv[2]
'''payload-the letter is sent to the server in the format of a dictionary in the payload'''
payload = {'our_letter': q}
response= requests.post(url=url, data=payload)

try:
    if not response.json:
        print('No result')
    else:
        id = response.json()['id']
        name = response.json()['name']
        
except ValueError:
    print('Not a valid JSON')

