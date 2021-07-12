import requests
import json

def getCountryCode(responseBody):
    results = responseBody["results"]
    country_codes = []
    for result in results:
        for address in result["address_components"]:
            if "country" in address["types"]:
                country_codes.append(address["short_name"])
    return country_codes

def get_data():
    rawContentFile = open("sample-country-request.json", "r")
    # data = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyCyc8DiRiBhhViBHfB62fYqkLkvn6i7W9Q&result_type=country')
    data = requests.get('http://www.mapquestapi.com/geocoding/v1/reverse?key=At1PEo3YjjPGG8BnrKg8DkCtgJkXKrWA&location=35.1728266,33.8942498').json()
    # rawContent = rawContentFile.read()
    # print(rawContent)
    print(data)
    # parsedRequest = json.load(rawContentFile)
    # rawContentFile.close()

    # print(getCountryCode(parsedRequest))

get_data()