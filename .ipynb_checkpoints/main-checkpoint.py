import matplotlib
import pandas as pd

df = pd.read_csv('data.csv')

#print(df.to_string())

#print(df['area'])
boxplot = df.boxplot(by='shape',column=['area'], grid=False)

boxplot