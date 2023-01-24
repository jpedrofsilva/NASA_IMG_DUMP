## This script downloads in bulk NASA's image of the day to a local directory
## Modifications should be made to "start_date" and "end_date" parameters as well as the directory location

import requests
import json
import webbrowser
import urllib.request
import ssl

#had to bypass ssl certification for https downloads to work
ssl._create_default_https_context = ssl._create_unverified_context

#API URL
url='https://api.nasa.gov/planetary/apod'
#API Key
key='SPeaDkD87BSV8tpEzbRU5ZAQkiREDAGKAMTM05Jv'

#API Parameters
params = {
    'start_date':'2022-01-21',
    'end_date':'2022-01-31',
    'hd':'True',
    'api_key': key
    }

#Store raw response data
response = requests.get(url, params=params)

#Convert response data to json
json_data = response.json()

#Iterate thru each dictionary in the json_data and downloads each image
for i in range(len(json_data)):
    #try needs to be used because some responses don't have a URL, this catches the error and continues the loop
    try:
        temp_url = json_data[i]['hdurl'] #stores image url in a str
        directory = "C:/Users/jps80/Downloads/NASADUMP/" + str(json_data[i]['date']) + ".jpg" #defines the directory to store each image
        urllib.request.urlretrieve(temp_url, directory) #downloads the image using the url and stores in directory
        print(json_data[i]['date']+" success")
        i=i+1
    except:
        print(json_data[i]['date']+" No img found") #error handling
