# The Weather Today

## Description
Small python script to fetch data from the [open weather map](https://openweathermap.org/) API.

## Installation
`pip install -r requirements.txt`

A folder etc/ need to be created containing a `config.ini` file with the following structure:  
```
[main]  
appid = openweathermapappid
```

## Usage
`python.exe wt.py {city_name} [-u] metric/kelvin`