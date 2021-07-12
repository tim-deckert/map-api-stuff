import pandas as pd
import requests
import json

BASE_URL="http://www.mapquestapi.com/geocoding/v1/reverse"
API_KEY=""

def readFeatures():
    return pd.read_csv('places_high_countries.csv')

def filterFeatures(feature):
    return feature[feature['country'] == '[]']

def geometryToLatlng(geometry):
    geometry = geometry.replace("'", "\"")
    print(geometry)
    geometryJson = json.loads(geometry)
    return f"{geometryJson['coordinates'][1]},{geometryJson['coordinates'][0]}"

def callRevGeocode(latlng):
    query = f'?key={API_KEY}&location={latlng}'
    fullUrl = BASE_URL+query
    print(f"Requesting: {fullUrl}")
    try:
        # rawContentFile = open("sampl-response-mapquest.json", "r")
        # parsedRequest = json.load(rawContentFile)
        # return parsedRequest
        return requests.get(fullUrl).json()
        return 
    except requests.exceptions.RequestException:
        raise RuntimeError("Error occurred during request") 

def getCountryCode(responseBody):
    results = responseBody["results"]
    country_codes = []
    for result in results:
        for location in result["locations"]:
            if "Country" == location['adminArea1Type']:
                country_codes.append(location["adminArea1"])
    return country_codes

def saveResponses(responses):
    with open("raw-country-codes.txt", "w") as outputFile:
        outputFile.writelines(responses)

features = filterFeatures(readFeatures())
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
    f2.to_csv("places_high_countries_missing.csv")
else:
    print(f'Responses size: {len(responses)}, Calculated size: {int(features.size / len(features.columns))}')