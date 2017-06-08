
import pandas as pd 

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
    
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[3, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[3, 9, 10, 11])

frames = [df1,df2,df3]
result = pd.concat(frames,keys=['x','y','z'])


print(result)
print(result.loc['x'])

#working on other axis
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                 'D': ['D2', 'D3', 'D6', 'D7'],
                  'F': ['F2', 'F3', 'F6', 'F7']},
                 index=[2, 3, 6, 7])
 
result = pd.concat([df1,df4],axis=1,join_axes=[df1.index])
print(result)

print('-'*100)
result_cat = pd.concat([df1,df4])
result_append = df1.append(df4)
print(result_cat)
print('-'*100)
print(result_append)
print('-'*100)

#series
s1 = pd.Series(['x0','x1','x2','x3'],name='X')
result = pd.concat([df1,s1],axis=1)
print(result)
print('-'*100)
result = pd.concat([df1,s1],axis=0)
print(result)

print('-'*100)
s3 = pd.Series([0, 1, 2, 3], name='foo')

s4 = pd.Series([0, 1, 2, 3])

s5 = pd.Series([0, 1, 4, 5])


result = pd.concat([s3,s4,s5],axis=1,keys=['red','orange','blue'])
print(result)
print('-'*100)

piece = {'x':df1,'y':df2,'z':df3}
result = pd.concat(piece)
print(result)


#Multiindex
print(result.index.levels)

#other levels
result = pd.concat([df1,df2,df3],keys=['x','y','z'],levels=[['z','y','x','w']],names=['group_key'])
print(result)

s2 = pd.Series(['x0','x1','x2','x3'],index=['A','B','C','D'])

result = df1.append(s2,ignore_index=True)
print(result)