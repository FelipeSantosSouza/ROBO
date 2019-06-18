import requests
import urllib3
headers = {'Content-type': 'application/json'}

url = 'http://ec2-52-14-112-85.us-east-2.compute.amazonaws.com:9000/insertInvetimento'
r = requests.post(url, data=open('jsonBmg.json', 'rb').read(), headers=headers)


