import pandas as pd
import requests
import json

BASE_URL="https://maps.googleapis.com/maps/api/geocode/json"
API_KEY="AIzaSyCyc8DiRiBhhViBHfB62fYqkLkvn6i7W9Q"
RESULT="country"

def readFeatures():
    with open('places_high.json',encoding='UTF-8') as jsonfile: 
        data = json.load(jsonfile)
    return pd.DataFrame(data['features'])

def geometryToLatlng(geometry):
    return f"{geometry['coordinates'][1]},{geometry['coordinates'][0]}"

def callRevGeocode(latlng):
    query = f'?latlng={latlng}&key={API_KEY}&result_type={RESULT}'
    fullUrl = BASE_URL+query
    print(f"Requesting: {fullUrl}")
    try:
        return requests.get(fullUrl).json()
    except requests.exceptions.RequestException:
        raise RuntimeError("Error occurred during request") 

def getCountryCode(responseBody):
    results = responseBody["results"]
    country_codes = []
    for result in results:
        for address in result["address_components"]:
            if "country" in address["types"]:
                country_codes.append(address["short_name"])
    return country_codes

def saveResponses(responses):
    with open("raw-country-codes.txt", "w") as outputFile:
        outputFile.writelines(responses)

features = readFeatures()
responses = []
entryNum = 0

for geometry in features['geometry']:
    latlng = geometryToLatlng(geometry)
    responseBody = callRevGeocode(latlng)
    countryCodes = getCountryCode(responseBody)
    if len(countryCodes) == 0:
        print(f"Error at entry {entryNum}:{features['geometry'][entryNum]}")
    responses.append(countryCodes)
    entryNum += 1

# saveResponses(responses)
print(responses)

if len(responses) == int(features.size / len(features.columns)):
    f2 = features.assign(country=responses)
    f2.to_csv("places_high_countries.csv")
else:
    print(f'Responses size: {len(responses)}, Calculated size: {int(features.size / len(features.columns))}')