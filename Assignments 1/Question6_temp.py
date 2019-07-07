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

from datetime import datetime

def fetchEPOCH(choice):
	x1=choice+' 00:00:00,010'
	x2=choice+' 23:59:59,010'
	dt_obj1 = datetime.strptime(x1,'%m/%d/%Y %H:%M:%S,%f')
	millisec1 = int(dt_obj1.timestamp() * 1000)
	dt_obj2 = datetime.strptime(x2,'%m/%d/%Y %H:%M:%S,%f')
	millisec2 = int(dt_obj2.timestamp() * 1000)
	return str(millisec1),str(millisec2)

choice=str(input('Enter the Date (format MM/DD/YYYY) : '))
start_date,end_date=fetchEPOCH(choice)
print(start_date)
print(end_date)

url1 = 'https://awm16002.srv.wifi.arista.com/new/webservice/V2/analytics/associationdata/'+start_date+'/'+end_date
print(url1)

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

response1 = requests.request("GET", url1, headers=headers1)
print(response1)

url2 = "https://awm16002.srv.wifi.arista.com/new/"+response1.text

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

response2 = requests.request("GET", url2, headers=headers2)

print(response2)

file = open('converter.csv', 'w')
file.write(response2.text)
file.close()

