import pandas as pd 
import numpy as np
# Data Frame

s1 = pd.Series([1,3], index = ['haha', 'hehe'])
s2 = pd.Series([2,4], index = ['haha', 'hehe'])
df1 = pd.DataFrame({'A': s1, 'B': s2})
print(df1)

sales = pd.Series([100, 150, 200, 250],
index=['Product A', 'Product B', 'Product C', 'Product D'])
cost = pd.Series(['80', '90', '120'], index=['Product A', 'Product B', 'Product C'])
units_sold = pd.Series(['20', 'S'], index=['Product A', 'Product D'])
df2 = pd.DataFrame({'Sales': sales, 'Cost': cost, 'Units Sold': units_sold})
print(df2)

data1 = [{'name': 'Emma', 'age': 28, 'city': 'Beijing'},
         {'name': 'Liam', 'age': 32, 'city': 'Shanghai'},
         {'name': 'Noah', 'age': 27, 'city': 'Guangzhou'}]
df3 = pd.DataFrame(data1)
print(df3)
print(df3["name"])

arr = np.array([[28, 32, 27],
                [1, 2, 3], 
                [1, 0, 1]])
df4 = pd.DataFrame(arr, columns=['Beijing', 'Shanghai', 'Guangzhou'],
                   index=['Age', 'ID', 'Service Available'])
print(df4)