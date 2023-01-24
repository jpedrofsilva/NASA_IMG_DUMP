## This script downloads NASA's image of the day in bulk to a local directory

import requests
import json
import webbrowser
import urllib.request
import ssl
import os
from dotenv import load_dotenv

#load .env file for importing API Key
load_dotenv()

#bypass ssl certification for https downloads to work
ssl._create_default_https_context = ssl._create_unverified_context

#API URL
url = 'https://api.nasa.gov/planetary/apod'
#API Key
key = os.getenv("API_KEY")

print("NASA Image Dump Script")

start_date = input("Input Start Date in YYYY-MM-DD:")
end_date = input("Input End Date in YYYY-MM-DD:")
directory = input("Input Download Directory:")

#API Parameters
params = {
    'start_date': start_date,
    'end_date': end_date,
    'hd':'True',
    'api_key': key
    }

#Store raw response data
response = requests.get(url, params=params)

#Convert response data to json
json_data = response.json()

#Iterate thru each dictionary in the json_data and download each image
for i in range(len(json_data)):
    #try needs to be used because some responses don't have a URL, this catches the error and continues the loop
    try:
        temp_url = json_data[i]['hdurl'] #stores image url in a string
        temp_directory = directory + "/" + str(json_data[i]['date']) + ".jpg" #defines the directory, file name, and file extension
        urllib.request.urlretrieve(temp_url, temp_directory) #downloads the image using the url and stores in directory
        print(json_data[i]['date']+" downloaded successfully")
        i=i+1
    except:
        print(json_data[i]['date']+" No image found") #error handling
