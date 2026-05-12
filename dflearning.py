import pandas as pd 
import numpy as np

def s1_series():
    ztf = np.ones(3)
    ztf = ztf.reshape(3,)
    ztff = np.array([22,33,44,55])
    s1 = pd.Series(ztff) # pd.Series 只接受一维数组
    return s1, s1.loc[2], s1.iloc[2]

def df1_dataframe(s1):
    s2 = pd.Series(['a', 'b', 'c'], index = [0,2,3])
    df1 = pd.DataFrame({"Score": s1, "Grades": s2})
    return df1

def get_dataframe(ztf1, ztf2):
    ztf1 = pd.Series([55,44,33,22,11], 
                    index = ['first', 'second', 'third', 'fourth', 'fifth'])
    ztf2 = pd.Series(['a', 'b', 'c', 'd', 'f'], 
                    index = ['first', 'second', 'third', 'fourth', 'fifth'])
    df2 = pd.DataFrame({'score': ztf1, 'grades': ztf2})
    return df2

s1, s1.loc[2], s1.iloc[2] = s1_series()
print(df1_dataframe(s1))