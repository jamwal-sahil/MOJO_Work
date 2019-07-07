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

url1 = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/devices/clients"

headers1 = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "0bdf46b9-a7fc-40d0-a7be-dafe1405f330,11166b29-8af0-43ff-a155-eb71a74dafb7",
    'Host': "awm16002.srv.wifi.arista.com",
    'Cookie': "JSESSIONID=22E95AE729DED106F391529AFE1855EA",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url1, headers=headers1)

print(response1)
data=response1.json()

import pandas as pd 
df=pd.DataFrame(data)
print(df)
df.to_csv("Visualize.csv", index = False)