import pandas as pd

def fun(MAC):
	df= pd.read_csv("conveter.csv")
	df.dropna(axis=1,inplace=True)
	newdf = df[df['Client MAC']==MAC]['SSID']
	print(newdf.unique())

#fun('90:2b:d2:2c:82:b8')
