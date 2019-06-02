import requests
import urllib3
url = 'http://ec2-18-222-220-54.us-east-2.compute.amazonaws.com:9000/insertInvetimento'
r = requests.post(url, data=open('jsonPan.json', 'rb'))
