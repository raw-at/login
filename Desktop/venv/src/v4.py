''' combining dataframes '''
import pandas as pd

df1 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},)

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7,8,9,6],
                    'Low_tier_HPI':[50, 52, 50, 53]},)
'''
#Concatenating
concat = pd.concat([df1,df2])
print(concat)
concat = pd.concat([df1,df2,df3])
print(concat)

df4 = df1.append(df3)
print(df4)

#appending
s = pd.Series([80,2,50],index=['HPI','Int_rate','US_GDP_Thousands'])
df4 = df1.append(s,ignore_index = True)
print(df4)

print('-'*50)
#merging 
print(df1)
print(df2)
print(pd.merge(df1,df2,on=["HPI","Int_rate"]))
'''
print('-'*50)

#JoininG

mergred = pd.merge(df1,df3,on='Year')
mergred.set_index('Year',inplace=True)
print(mergred)

print(df1.join(df3))






