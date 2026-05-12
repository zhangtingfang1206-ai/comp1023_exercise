import pandas as pd

s1 = pd.Series([1,2,3,4,5], 
               index =['a', 'b', 'c', 'd', 'e'] )
mask = (s1 > 2) & (s1 < 10)
print(mask, type(mask))   # bool <class 'pandas.Series'>
s1[mask] = 0
print(s1)