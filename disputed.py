import pandas as pd

df = pd.read_csv('places_high_countries.csv')
df2 = df[df['country'] == '[]']
df2.to_csv('missingCountryEntries.csv')

print(coords.size)