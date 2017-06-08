import pandas as pd 
import quandl 

api_key = open('quandlapikey.txt','r').read()

df = quandl.get("FMAC/HPI_MD", authtoken=api_key) 


fifty_stats = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

print(fifty_stats[0][0]) 
for abbv in fifty_stats[0][0][1:]:
    print("FMAC/HPI_"+str(abbv))

