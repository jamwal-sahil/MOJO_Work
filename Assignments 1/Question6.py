
import requests

url = "https://awm16002.srv.wifi.arista.com/new/webservice/login/modScanWifi/86400"

payload = "{\n\"type\":\"apikeycredentials\",\n\"keyId\":\"KEY-ATN565039-674\",\n\"keyValue\":\"16d7b32456a7700568d359fa452818bd\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "305e8595-dcd0-4d7b-82c7-0b27f86ba1fe"
    }

response = requests.request("POST", url, data=payload, headers=headers)

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
df = df.loc[:, df.columns.intersection(['Association Start Time Local','Association End Time Local'])]
df.sort_values(['Association Start Time Local'], ascending=True,inplace=True)
df['Start Date'], df['Start Time'] = df['Association Start Time Local'].str.split(' ', 1).str
df['End Date'], df['End Time'] = df['Association End Time Local'].str.split(' ', 1).str
df = df.drop(df.columns[[0, 1]], axis=1)
choice=str(input('Enter the Date (format MM/DD/YYYY) : '))
df=df[df['Start Date']==choice]

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
df['Start Time']=df['Start Time'].apply(get_sec)
df['End Time']=df['End Time'].apply(get_sec)

df['interval'] = df[['Start Time', 'End Time']].values.tolist()
interval = df["interval"].tolist()

interval.sort(key=lambda interval: interval[0])
merged = [interval[0]]
for current in interval:
    previous = merged[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged.append(current)

for i in range(len(merged)):
    merged[i]=merged[i][1]-merged[i][0]

idle_time=int(86400-sum(merged))
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d hours %02d minutes %02d seconds" % (hour, minutes, seconds)

print('Time duration when there was no client connected to the AP ::::::::',convert(idle_time))