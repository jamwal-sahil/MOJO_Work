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

url = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/devices/clients/0/25"

querystring = {"capability":"97","id":"%0A0","sortcolumn":"Computer_Lab_C_9E:1F","sortascending":"false%0A"}

headers3 = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a0325df0-5e50-4183-a741-aeca4a065a05,d17234d8-746d-4414-9466-f85d76bb900f",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response3 = requests.request("GET", url, headers=headers3, params=querystring)

print(response3)
data=response3.json()

import pandas as pd 
df=pd.DataFrame(data)

def fetchMAC(x):
     return x['radios'][0]['macaddress']
df['totalCount']=df['clientList'].apply(fetchMAC)

def fetchNAME(x):
     return (x['name'])
df['nextLink']=df['clientList'].apply(fetchNAME)

def fetchBOXID(x):
     return (x['boxId'])
df['previousLink']=df['clientList'].apply(fetchBOXID)

def fetchTYPE(x):
     return (x['type'])
df['clientList']=df['clientList'].apply(fetchTYPE)

df.rename(columns={'clientList':'type','previousLink':'boxId','nextLink':'name','totalCount':'MACaddress'},inplace=True)

print('List of all Client connected to APs at a given location : (Total Count = ',df['type'].count(),')')
print(df)

#df.to_csv("ListAPs.csv", index = False)