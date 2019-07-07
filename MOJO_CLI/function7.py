import pandas as pd
import numpy as np

def fun(MAC):
	df= pd.read_csv("conveter.csv")
	df.dropna(axis=1,inplace=True)
	newdf = df[df['Client MAC']==MAC]['Data Transferred To Device (Bytes)']
	newdf=newdf/(1024*1024)
	print(newdf)

#fun('90:32:4b:8f:84:5b')
