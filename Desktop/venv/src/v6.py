import pandas as pd
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3'],
                         'key': ['K0', 'K1', 'K0', 'K1']})
    

right = pd.DataFrame({'C': ['C0', 'C1'],
                          'D': ['D0', 'D1']},
                          index=['K0', 'K1'])


result = pd.merge(left,right, left_on='key',how='left',right_index=True)
print(result)