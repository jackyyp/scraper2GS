import pandas as pd

df = pd.read_csv('data.csv', delimiter=',',dtype=str)
df = df.drop(df.columns[[1,2,8,9]],axis=1)
df = df.rename(columns={'Unnamed: 0' :'Rank'})


