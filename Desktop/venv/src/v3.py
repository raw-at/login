import pandas as pd 
import quandl 
import pickle  #save any python object
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt','r').read()



def state_list():

    fifty_stats = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_stats[0][0][1:]

def grab_initial_data():
    state = state_list()
    main_df = pd.DataFrame()

    for abbv in state:
        query = "FMAC/HPI_"+str(abbv)
        
        df = quandl.get(query,authtoken=api_key)
        df.columns = [str(abbv)]
        df[abbv] = (df[abbv]-df[abbv][0])/df[abbv][0] * 100
         
        if main_df.empty: 
            main_df = df
        else:
            main_df = main_df.join(df);
        
    print(main_df.head())

    pickle_out = open('fifty_stats3.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA',authtoken=api_key)
    df.rename(columns={'Value':'United States'},inplace=True)
    df['United States'] = (df['United States']-df['United States'][0])/df['United States'][0]*100.0
    return df
    

#grab_initial_data()
fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0),sharex=ax1)



#pickle_in = open('fifty_stats.pickle','rb')
#HPI_data = pickle.load(pickle_in)
#print(HPI_data)


#Pandas pickling

#HPI_data.to_pickle('pickle.pickle')

HPI_data = pd.read_pickle('fifty_stats3.pickle')

TX_AK_12corr = pd.rolling_corr(HPI_data['TX'],HPI_data['AK'],12)
HPI_data['TX'].plot(ax=ax1,label='TX HPI')
HPI_data['AK'].plot(ax=ax1,label='Ak HPI')

ax1.legend(loc=4)
TX_AK_12corr.plot(ax=ax2,label='correlation TX and AK')


#print(HPI_data)

# TX12MA = HPI_data['TX'].resample('A',how='mean')

#print( TX12MA.head())

#print(HPI_data2)
#benchmark = HPI_Benchmark()
#benchmark.plot(ax=ax1,color='k',linewidth=20)
#Modify column
#HPI_data['TX12MA'] =  pd.rolling_mean(HPI_data['TX'],12)
#HPI_data['TX12STD'] =  pd.rolling_std(HPI_data['TX'],12)
#print(HPI_data[['TX','TX12MA','TX12STD']].head())

#drop NaN

#HPI_data.dropna(inplace=True)
#FIll Nan
#HPI_data.fillna(-99999,limit=10,inplace=True)

#print(HPI_data[['TX',' TX12MA']].head())

#HPI_data[['TX','TX12MA','TX12STD']].plot(ax=ax1)
#HPI_data[['TX12STD']].plot(ax=ax2)
plt.legend(loc=4)
plt.show()


'''correlation

HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)

print(HPI_State_Correlation.describe())
'''

#handling missing data NAN















