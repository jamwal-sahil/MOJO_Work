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

url2 = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/devices/clients/0/25"

querystring = {"capability":"97","id":"%0A2","sortcolumn":"Computer_Lab_C_9E:1F","sortascending":"false%0A"}

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "2bfd9cba-ba52-43d0-8aef-3c85d33c6db7,deed6add-6f85-4e90-a388-c4c17c6f545b",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url2, headers=headers2, params=querystring)

print(response2)
data=response2.json()

import pandas as pd 
df=pd.DataFrame(data)

def fetchBAND(x):
     return x['bandCapability']
df['totalCount']=df['clientList'].apply(fetchBAND)

def fetchNAME(x):
     return (x['name'])
df['nextLink']=df['clientList'].apply(fetchNAME)

def fetchBOXID(x):
     return (x['boxId'])
df['previousLink']=df['clientList'].apply(fetchBOXID)

def fetchTYPE(x):
     return (x['type'])
df['clientList']=df['clientList'].apply(fetchTYPE)

df.rename(columns={'clientList':'type','previousLink':'boxId','nextLink':'name','totalCount':'Band Capability'},inplace=True)
print("Number of clients in dualBand mode : ",len(df[df["Band Capability"]=='CAPABILITY_DUAL_BAND']))
print("Number of clients in 2.4GHz Band mode : ",len(df[df["Band Capability"]=='CAPABILITY_2_4_GHZ']))
print("Number of clients in 5GHz Band mode : ",len(df[df["Band Capability"]=='CAPABILITY_5_GHZ']))
print("Number of clients in Unknown mode : ",len(df[df["Band Capability"]=='UNKNOWN']))
print(df)
#df.to_csv("ListAPs.csv", index = False)