import pandas as pd
import os

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'],
index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000],
index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4],
index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population,
'Area (sq km)': area})
print(df) # Display the original DataFrame
# Drop the 'Population' and 'Area (sq km)' columns
df = df.drop(columns=['Population'])

print(df)
df1 = pd.DataFrame(df)
path = os.path.join('./df1', 'employees1.csv')
df1.to_csv(path, sep = ',', index = False) # index is the row names