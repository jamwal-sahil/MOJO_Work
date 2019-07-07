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

url = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/locations/tree"

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5fab8d39-53b4-4261-83e9-0f9865f3e1ed,7291fc36-ca1b-45a1-96f9-b9516c07f617",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url, headers=headers2)

print(response2)

url = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/devices/aps"

headers3 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "064a2a2f-bee7-4bfb-9732-7c5cf23a8e5d,a9cbdd2b-cc59-48ca-bfb0-0901a2d188f6",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response3 = requests.request("GET", url, headers=headers3)

data=response3.json()

import pandas as pd 
df=pd.DataFrame(data)
df = df.loc[:, df.columns.intersection(['type','boxId','name','locationId','radios'])]
df=df[['type','boxId','name','locationId','radios']]

def fetchLocation(x):
    return x['id']
df['locationId']=df['locationId'].apply(fetchLocation)


def fetchMAC(x):
     return x[0]['macaddress']
df['radios']=df['radios'].apply(fetchMAC)
df.rename(columns={'radios':'MACaddress'},inplace=True)

print('List of APs present at a location(Id=2) : (Total Count = ',df['type'].count(),')')
print(df)
#df.to_csv("ListAPs.csv", index = False)