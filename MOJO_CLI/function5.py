import pandas as pd
import numpy as np

def fun(MAC):
	df= pd.read_csv("conveter.csv")
	df.fillna(value='NONE',inplace=True)
	newdf = df[df['Client MAC']==MAC]['Domains Accessed']
	pd.set_option('max_colwidth', -1)
	print(newdf)

#fun('90:32:4b:8f:84:5b')

