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

url = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/clients/statistics/averagelatencies?clientmacaddress="+mac

headers1 = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "979c17ac-921d-4820-a6ac-92966f465f40,ee1cbac4-863f-4e10-b8e1-43f282596c5c",
    'Host': "awm16002.srv.wifi.arista.com",
    'Cookie': "JSESSIONID=B45FC05A5B8DB29358B03835469D4D1D",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url, headers=headers1)
print(response1)
data=response1.json()
print('Average AAA Latency of Client ::::',data['averageAaaLatency'])
print('Average DHCP Latency of Client ::::',data['averageDhcpLatency'])
print('Average DNS Latency of Client ::::',data['averageDnsLatency'])