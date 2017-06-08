#IO basics

import pandas as pd 
df = pd.read_csv('testData.csv')
print(df.head())

df.set_index('Date',inplace=True)

df.to_csv('newtestData.csv')

df = pd.read_csv('newtestData.csv')
print(df.head())


df = pd.read_csv('newtestData.csv',index_col = 0)
print(df.head())

#rename all column

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('newcsv3.csv')

df.to_csv('newcsv4.csv',header=False) #no headers only data

df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'],index_col = 0)
print(df.head())

#csv to other(HTML table)

df.to_html('example.html')


df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'},inplace=True)
print(df.head())
