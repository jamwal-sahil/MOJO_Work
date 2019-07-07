import requests

url = "https://awm16002.srv.wifi.arista.com/new/webservice/login/modScanWifi/86400"

payload = "{\"type\":\"apikeycredentials\",\"keyId\":\"KEY-ATN565039-674\",\"keyValue\":\"16d7b32456a7700568d359fa452818bd\"}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "9ff876ba-5976-45ef-b229-54727c749ccf,f8e9171c-c4ff-4a6f-8687-044ff91ac551",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=97FF83CBA16E91DEC25CF9B5D8E7383F",
    'accept-encoding': "gzip, deflate",
    'content-length': "102",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

import time
milliseconds = str(round(time.time() * 1000))


url1 = "https://awm16002.srv.wifi.arista.com/new/webservice/v2/analytics/visibilitydata/1560709800000/"+milliseconds

headers1 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ecc94f00-ecab-4342-a5bf-16473f424c2d,b55a9b50-b8f7-42e7-9cb7-482838db4dbc",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=501F8DF66C90198FD8FAECA68BADBAB1",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url1, headers=headers1)
print(response1)
url2 = "https://awm16002.srv.wifi.arista.com/new/"+ response1.text

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e6f6b693-2cb5-4269-9d5e-53ab2dc69ebc,d8bf7842-7400-4281-a83f-8835842328f2",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=501F8DF66C90198FD8FAECA68BADBAB1",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url2, headers=headers2)
print(response2)
file = open('RSSI.csv', 'w')
file.write(response2.text)
file.close()

import pandas as pd
df= pd.read_csv("RSSI.csv")
df.dropna(axis=1,inplace=True)
print("Number of clients whose RSSI is less than -75 dBM : ",len(df[df["Best RSSI"]<(-75)]['Client MAC'].unique()))
print(df[df["Best RSSI"]<(-75)][['Client MAC','Best RSSI']])