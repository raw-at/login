import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {
    'day':[1,2,3,4,5,6],
    'visitors':[43,52,36,5,4,12],
    'Bounce_rate':[65,4,5,64,75,66]
    
    }

#Dict to dataframe

df = pd.DataFrame(web_stats)

'''
print(df)

print(df.head()) #print top five
print(df.tail()) #print last five
print(df.tail(2)) #last two
'''

#df = df.set_index('day')
df.set_index('day',inplace=True)

#print(df.set_index('day'))
print(df.head())

#getting info column wise
print(df['visitors'])
print(df['Bounce_rate'])

#multiple column
print(df[['visitors','Bounce_rate']])


print(df.visitors.tolist())
#print(df[['visitors','Bounce_rate']].tolist()) this gives error
print(np.array(df[['visitors','Bounce_rate']]))

df2 = pd.DataFrame(np.array(df[['visitors','Bounce_rate']]))
print(df2)