import pandas as pd
import json

# # df = pd.read_json('places_high.json',encoding='utf-8')
# with open('places_high.json',encoding='UTF-8') as jsonfile: 
#     # rawData = jsonfile.read()
#     # rawSlice = rawData[897830:897840]
#     # print(rawSlice)
#     data = json.load(jsonfile)

# df = pd.DataFrame(data['features'])
dcf = pd.read_csv('places_high_features.csv')
# print(df.size)
print(dcf.columns)
print(dcf.size / len(dcf.columns))

# df.to_csv('places_high_features.csv')

# for geometry in df['geometry']:
#     print(f"{geometry['coordinates'][1]},{geometry['coordinates'][0]}")
#     print(geometry['coordinates'])
#     break