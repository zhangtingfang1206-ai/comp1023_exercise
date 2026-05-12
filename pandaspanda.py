import pandas as pd   # we can name the data separately
# pandas series (1D)
import numpy as np

a = np.array(([1,2,3],
              [4,5,6]))
s1 = pd.Series([10, 20, 30, 40])
print(s1[0])
print()
s2 = pd.Series([10, 20, 30, 40], 
               index = ["fruit", 'd','d','er'])
data = {'first': 10, 'second': 20, 'third': 30, 'fourth': 40}
s3 = pd.Series(data)
e1 = s3.loc['second'] # location
e2 = s3.iloc[2]    # index location
print(e1); print(e2)
print(s3.values, type(s3.values))    
print(s3.index, type(s3.index))    # <class 'pandas.Index'>

# change values:
s2 = pd.Series([10, 20, 30, 40], 
               index = ["fruit", 'd','d','er'])
s2.loc['d'] = 100
print(s2)
'''
                fruit     10
                d        100
                d        100
                er        40
                dtype: int64
                '''