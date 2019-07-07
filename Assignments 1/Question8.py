import requests

url = "https://awm16002.srv.wifi.arista.com/new/webservice/login/modScanWifi/86400"

payload = "{\n\"type\":\"apikeycredentials\",\n\"keyId\":\"KEY-ATN565039-674\",\n\"keyValue\":\"16d7b32456a7700568d359fa452818bd\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "305e8595-dcd0-4d7b-82c7-0b27f86ba1fe"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response)

import time
milliseconds = str(round(time.time() * 1000))

url = "https://awm16002.srv.wifi.arista.com/new/webservice/V2/analytics/associationdata/1560709800000/"+milliseconds
#Start DateTime Mon Jun 17 2019 00:00:00 GMT+0530
#End DateTime current system datetime

headers1 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "9a636299-5b45-4c46-906b-3bad8d1b596f,bb3133ff-6a62-4b4b-8d90-864538ff8565",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url, headers=headers1)
print(response1)

url = "https://awm16002.srv.wifi.arista.com/new/"+response1.text

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5444a130-20fa-4e28-b839-4f465937b216,03d96b54-5201-42a8-81b7-42e839f63e9d",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url, headers=headers2)

print(response2)

file = open('conveter.csv', 'w')
file.write(response2.text)
file.close()

import pandas as pd
df= pd.read_csv("conveter.csv")
df = df.loc[:, df.columns.intersection(['Client MAC','Data Rate (kbps)'])]
df=df.groupby('Client MAC').mean()
newdf=df[df["Data Rate (kbps)"]>153600]
print('Number of users with avg. data rate greater than 150 Mbps =',len(newdf))
print(newdf)
#newdf.to_csv("Visualize.csv")