import requests
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

url = "https://awm16002.srv.wifi.arista.com/new/webservice/login/modScanWifi/86400"

payload = "{\n\"type\":\"apikeycredentials\",\n\"keyId\":\"KEY-ATN565039-674\",\n\"keyValue\":\"16d7b32456a7700568d359fa452818bd\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "305e8595-dcd0-4d7b-82c7-0b27f86ba1fe"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response)

url1 = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/manageddevices/statistics/trend"

querystring1 = {"devicecategory":"MANAGED_AP","type":"apdatatransferhistory","boxid":"38733937","fromtime":"1561865400000","totime":"1561872600000"}

headers1 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "3093e910-29db-43a5-8710-fb13551787a7,d43e322f-11c1-470e-821c-0e55b74030a9",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response1 = requests.request("GET", url1, headers=headers1, params=querystring1)
plt.figure(figsize=(12,6))

print(response1)
data1=response1.json()
df1=pd.DataFrame(data1['samples'])
plt.subplot(221)
plt.plot(df1['time'],df1['value'],'-o',label='Performance Trend (APdataTransferHistory)')
plt.xlabel('Time (milliseconds)')
plt.ylabel('DataRate (Kbps)')
plt.title('Time vs DataRate')
plt.legend(loc='best')


url2 = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/clients/statistics/trend"

querystring2 = {"type":"clientdatarate","ssid":"IIT_JAMMU","boxid":"42307944"}

headers2 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "08a6e481-f86b-4410-8d4a-98e2eca929c2,b7096324-224b-4185-9714-69c20370acbf",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response2 = requests.request("GET", url2, headers=headers2, params=querystring2)
print(response2)
data2=response2.json()
df2=pd.DataFrame(data2['samples'])
plt.subplot(222)
plt.plot(df2['time'],df2['value'],'-og',label='Performance Trend (ClientDataRate)')
plt.xlabel('Time (milliseconds)')
plt.ylabel('DataRate (Kbps)')
plt.title('Time vs DataRate')
plt.legend(loc='best')

url3 = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/clients/statistics/trend"

querystring3 = {"type":"clienttraffic","ssid":"IIT_JAMMU","boxid":"42307944"}

headers3 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "10c21efd-b0af-4db8-af5e-eb41b3324b75,6d398abe-0edd-4683-a3ad-d14a314351df",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response3 = requests.request("GET", url3, headers=headers3, params=querystring3)
print(response3)
data3=response3.json()
df3=pd.DataFrame(data3['samples'])
plt.subplot(223)
plt.plot(df3['time'],df3['value'],'-ob',label='Performance Trend (ClientTraffic)')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Data (Kb)')
plt.title('Time vs Data')
plt.legend(loc='best')

url4 = "https://awm16002.srv.wifi.arista.com/new/webservice/V3/devices/clients/statistics/trend"
querystring4 = {"type":"clientretransmissionrate","ssid":"IIT_JAMMU","boxid":"42307944"}

headers4 = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "470818e2-adab-4d7c-b58d-dfcfd8b6c331,b4021fbd-1cf6-464a-ad81-58277f667647",
    'Host': "awm16002.srv.wifi.arista.com",
    'cookie': "JSESSIONID=6B5FD4483136C519C5305F3EB2C5C1E4",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response4 = requests.request("GET", url4, headers=headers4, params=querystring4)
print(response4)
data4=response4.json()
df4=pd.DataFrame(data4['samples'])
plt.subplot(224)
plt.plot(df4['time'],df4['value'],'-oc',label='Performance Trend (ClientRetransmissionRate)')
plt.xlabel('Time (milliseconds)')
plt.ylabel('DataRate (Kbps)')
plt.title('Time vs DataRate')
plt.legend(loc='best')
plt.tight_layout()
plt.show()