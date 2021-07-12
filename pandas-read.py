import pandas as pd
import json

with open('places_high.json',encoding='UTF-8') as jsonfile: 
    data = json.load(jsonfile)

# df = pd.DataFrame(data['features'])
dcf = pd.read_csv('places_high_features.csv')

# df.to_csv('places_high_features.csv')

# for geometry in df['geometry']:
#     print(f"{geometry['coordinates'][1]},{geometry['coordinates'][0]}")
#     print(geometry['coordinates'])
#     break