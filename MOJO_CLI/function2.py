import pandas as pd
import numpy as np

def fun(MAC):
	df= pd.read_csv("conveter.csv")
	df.dropna(axis=1,inplace=True)
	newdf = df[df['Client MAC']==MAC][['Association Start Time (GMT)','Session Duration']]
	print(newdf)

#fun('90:2b:d2:2c:82:b8')
