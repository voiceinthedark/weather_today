import configparser
from datetime import datetime
from argparse import ArgumentParser
import requests

def get_request(q, units='metric'):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    cnf = configparser.ConfigParser()
    cnf.read('etc/config.ini')
    appid = cnf.get('main', 'appid')
    geoid = cnf.get('main', 'geoid')
    units = units

    if q == 'geo':
        rg = requests.get('https://api.ipdata.co?', params={'api-key': geoid})
        # print(rg.json())
        resg = rg.json()
        q = resg['city']
    
    r = requests.get(url, params={'q': q, 'units': units, 'appid': appid,})
    if r.status_code == 200:
        jsn_res = r.json()
        __filter_response(jsn_res, temp_unit='C' if units == 'metric' else 'K')        
    else:
        print('Trouble connecting to server')    

def __filter_response(jsn, temp_unit='C'):
    city = jsn['name']
    tm = datetime.fromtimestamp(jsn['dt'])
    overcast = jsn['weather'][0]['description']
    temp = jsn['main']['temp']
    temp_feel = jsn['main']['feels_like']
    temp_min = jsn['main']['temp_min']
    temp_max = jsn['main']['temp_max']
    humidity = jsn['main']['humidity']
    wnd_speed = jsn['wind']['speed']
    sunrise = datetime.fromtimestamp(jsn['sys']['sunrise']).strftime("%H:%m")
    sunset = datetime.fromtimestamp(jsn['sys']['sunset']).strftime("%H:%m")

    res = f"""Weather forecast for {city} at {tm}
    Overcast:        {overcast}
    Temperature:     {temp}°{temp_unit} -- {temp_feel}°{temp_unit}
    Min Temperature: {temp_min}°{temp_unit} -- Max Temperature: {temp_max}°{temp_unit}
    Humidity:        {humidity}  
    Wind speed:      {wnd_speed} m/s
    Sunrise:         {sunrise}  
    Sunset:          {sunset}
    """
    print(res)


if __name__ == "__main__":    
    parser = ArgumentParser("The Weather Today")
    parser.add_argument('-c', '--city', help="city to fetch weather forecast")
    parser.add_argument('-u', '--unit', default='metric', help="unit of degrees metric/kelvin")
    args = parser.parse_args()

    g = 'geo'
    if args.city:
        g = args.city
    get_request(q=g, units=args.unit)
