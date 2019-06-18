import requests
import urllib3
import json

with open('jsonBmg.json') as json_file:
    json_data = json.load(json_file)

for linha in json_data:
    print(linha)

headers = {'Content-type': 'application/json'}

url = 'http://ec2-52-14-112-85.us-east-2.compute.amazonaws.com:9000/insertInvetimento'
r = requests.post(url, json=json_data, headers=headers)
print("Saida do POST")
print(r.text)

