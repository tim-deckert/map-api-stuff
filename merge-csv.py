import pandas as pd
import numpy as np

df = pd.read_csv('places_high_countries.csv')
df2 = pd.read_csv('places_high_countries_missing.csv')
df2 = df2.filter(items=['id','type','properties','geometry','country'])

df2.set_index(df2['id'], inplace=True)
df.loc[df2['id'], ['country']] = df2['country']

df[['type','properties','geometry','country']].to_csv("clean-countries.csv")