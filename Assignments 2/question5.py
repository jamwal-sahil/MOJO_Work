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

url1 = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/clients/0/25"

querystring1= {"filter":"{ \"property\": \"capability\",\"value\": [3],\"operator\": \"=\"}"}

headers1 = {
    'Content-Type': "application/jsons",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "432f1350-4a80-4e9c-9a10-84b0bfd1ac84,7f6bd175-0e1c-48b3-87fd-37d12384687d",
    'Host': "awm16002.srv.wifi.arista.com",
    'Cookie': "JSESSIONID=22E95AE729DED106F391529AFE1855EA",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url1, headers=headers1, params=querystring1)

print(response1)
data=response1.json()

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
print('List of Clients which support 802.11ac protocol ::::')
print(df)


url2 = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/clients/0/25"

from datetime import timedelta    
import datetime
t4_hours_ago = datetime.datetime.now() - datetime.timedelta(minutes=1440)
t4_hours_ago_milliseconds = str(round(t4_hours_ago.timestamp() * 1000))
print('\n\nFrom Time(ms) : ',t4_hours_ago_milliseconds)

import time
milliseconds = str(round(time.time() * 1000))
print('End Time(ms) : ',milliseconds) #System's current time

querystring2 = {"performancestarttime":t4_hours_ago_milliseconds,"performanceendtime":milliseconds,"filter":"{ \"property\": \"capability\",\"value\": [3],\"operator\": \"=\"}","historicfrequencyband":"2.4"}

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d4443870-77ac-47d2-a808-133f2802db17,d7ce5f06-b497-49bd-8bc5-7ebc2206dc29",
    'Host': "awm16002.srv.wifi.arista.com",
    'Cookie': "JSESSIONID=22E95AE729DED106F391529AFE1855EA",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url2, headers=headers2, params=querystring2)
print(response2)
data=response2.json()

import pandas as pd 
df=pd.DataFrame(data)
def fetchCradio(x):
     return x['radios'][0]['clientsCountOfAssocRadio']
df['clientsCountOfAssocRadio']=df['clientList'].apply(fetchCradio)

def fetchCap(x):
     return x['radios'][0]['observedBssidsCountByAssocAP']
df['observedBssidsCountByAssocAP']=df['clientList'].apply(fetchCap)

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
print('No of times a client connected on 2.4GHz band in last 24hours ::::')
print(df)
#df.to_csv("Visualize.csv", index = False)