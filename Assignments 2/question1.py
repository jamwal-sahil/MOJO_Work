import requests
import json

url = "https://awm16002.srv.wifi.arista.com/new/webservice/login/modScanWifi/86400"

payload = "{\n\"type\":\"apikeycredentials\",\n\"keyId\":\"KEY-ATN565039-674\",\n\"keyValue\":\"16d7b32456a7700568d359fa452818bd\"\n}"
headers1 = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "305e8595-dcd0-4d7b-82c7-0b27f86ba1fe"
    }

response = requests.request("POST", url, data=payload, headers=headers1)
print(response)

mac=str(input('Enter the MAC Address of your Device : '))

url1 = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/associations/infrastructure/clients/"+mac

headers1 = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "dfc0b174-b198-4fa0-9257-1908be3da2a5,618f7525-ea37-4b21-aa63-59d42491cdee",
    'Host': "awm16002.srv.wifi.arista.com",
    'Cookie': "JSESSIONID=B45FC05A5B8DB29358B03835469D4D1D",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url1, headers=headers1)

print(response1)

data=response1.json()

print('MAC Address of the connected AP ::::',data['primaryRadio']['macaddress'])
print('Name of the connected AP ::::',data['name'])
print('Box Id of the connected AP ::::',data['boxId'])