import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def fun():
	df= pd.read_csv("conveter.csv")
	df1=df.dropna(axis=1, how='any', thresh=None, subset=None, inplace=False)
	#df1.to_csv("edited.csv",index=False)
	sns.pairplot(df1,dropna=True,hue='SSID',diag_kind='hist')
	plt.show()

#fun()