# The Weather Today

## Description
Small python script to fetch data from the [open weather map](https://openweathermap.org/) API.  
And the [ipdata.co](https://www.ipdata.co) for geolocation.

## Requirements
A free account in [open weather map](https://openweathermap.org/) for the API key; as well as free account in [ipdata.co](https://www.ipdata.co) for the apikey for geolocation feature.


## Installation
`pip install -r requirements.txt`

A folder etc/ need to be created containing a `config.ini` file with the following structure:  
```
[main]  
appid = openweathermapappid
geoid = ipdataapikey
```

## Usage
`python.exe wt.py [-c] {city_name} [-u] metric/kelvin`  
If no `-c` city argument was given, the program will geolocate your location and fetch the required data.
