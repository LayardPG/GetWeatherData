 #/usr/bin/python3
#getGetWeather.py - Prints the weather for a location from the command line

APPID = '05c13fbd098bf9bf58ae5c31a71624d6'

import json, requests, sys

#Compute location from command line arguments
if len(sys.argv)<2:
	print('usage: getOpen GetWeather.py city_name, 2-letter_country_code')
	sys.exit()
location = ''.join(sys.argv[1:]) # create a string variable by joining all elements of the sys.argv list
# using the join method available in the string data type.

# TODO: Download the JSON data from Open WeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s'% (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)

# TODO: Load JSON data into a Python variable
