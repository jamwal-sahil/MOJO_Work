import requests
import json

url = "https://awm16002.srv.wifi.arista.com/new/webservice/login/modScanWifi/86400"

payload = "{\n\"type\":\"apikeycredentials\",\n\"keyId\":\"KEY-ATN565039-674\",\n\"keyValue\":\"16d7b32456a7700568d359fa452818bd\"\n}"
headers1 = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "305e8595-dcd0-4d7b-82c7-0b27f86ba1fe"
    }

response1 = requests.request("POST", url, data=payload, headers=headers1)
print(response1)

url2 = "https://awm16002.srv.wifi.arista.com/new/webservice/v3/devices/clients/15469568/observingmanageddevices"

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a4e3640a-47a6-4338-ade1-6a8134e6fe7f,62d77180-41a1-4773-8f38-bff934a12ee0",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url2, headers=headers2)

print(response2)
data=response2.json()

import pandas as pd 
df=pd.DataFrame(data)
df=df[['boxId','name','numClients2_4Ghz','numClients5Ghz']]

print('List of APs visible to a specific Client(Box Id=541422522) : (Total Count = ',len(df),')')
print(df)
#df.to_csv("ListAPs.csv", index = False)