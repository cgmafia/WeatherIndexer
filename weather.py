import os
from re import A
import requests
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
dotenv_path = Path('.env')

class Weather:
    def get_index_weather_now():
        index_city = os.getenv('INDEX_CITY')
        index_url = os.getenv('OpenWeatherAPI') + '?q=' + index_city + '&units=metric&appid=' + os.getenv('API_KEY')
        index_weather = requests.get(index_url)
        index_weather = index_weather.json()
        index_temp = index_weather['main']['temp']
        return index_temp

    def check_even_characters(city):
        if len(city) % 2 == 0: 
            return True
        else: 
            return False
    
    def check_valid_city(city):
        checkURL = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+ os.getenv('API_KEY')
        city_check = requests.get(checkURL)
        city_check = city_check.json()
        if city_check['message']:
            message = city_check['message']
            if  message == "Not found city":
                return False
            else:
                return True
        else:
            return False

    def get_weather(city):
        checkURL = os.getenv('OpenWeatherAPI') + '?q=' + city + '&units=metric&appid=' + os.getenv('API_KEY')
        data = requests.get(checkURL, city)
        weather = data.json()
        city_temprature = weather['main']['temp']
        sunrise_time = weather["sys"]["sunrise"]
        sunset_time =  weather["sys"]["sunset"]
        now = weather['dt']
        result = {
            "city": city,
            "city_temprature" : city_temprature,
            "sunrise_time" : sunrise_time,
            "sunset_time": sunset_time,
            "now": now
        }
        return result

    def get_rival(city):
        index_city_temp = Weather.get_index_weather_now()
        city_temp = Weather.get_weather(city)
        city_temp = city_temp['city_temprature']
        if index_city_temp <= city_temp: return True
        else: return False

    def get_daytemp(data):
        if data['sunset_time'] > data['now'] < data['sunrise_time']:
            if 17 < data['city_temprature'] < 27:
                return True
            else:
                return False
        else:
            if 10 < data['city_temprature'] < 15:
                return True
            else:
                return False


    def formulate_response(city):
        weatherdata = Weather.get_weather(city)
        daytemp_res = Weather.get_daytemp(weatherdata)
        naming = Weather.check_even_characters(city)
        rival = Weather.get_rival(city)
        d = {
            "check": True,
            "criteria": {
                "naming": naming,
                "daytemp": daytemp_res,
                "rival": rival
            }
        }
        return d

def main(city_name):
    result = Weather.formulate_response(city_name)
    return result
