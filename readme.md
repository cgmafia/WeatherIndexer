## Test to check the weather
This API respose has been developed according to the requirement
I have taken the index city as Cologne for rival comparison


## Requirements & Installation

 - [x] Python 3.9+
 - [x] Flask
 - [x] Pytest

#### Steps to install
1. Make sure you have Python 3.9 and above installed
2. cd to this directory
3. create a `.env` file in the root with following parameters:
```
    OpenWeatherAPI=http://api.openweathermap.org/data/2.5/weather
    API_KEY=Your API key
    INDEX_CITY = City you want to index with
```

4. To install all the requirements, run `pip install -r requirements.txt`
5. To run the API run `python api.py`
6. To run tests run `python -m pytest`

## Endpoints
 - http://localhost:5000/
 - http://localhost:5000/check
 - http://localhost:5000/check?city=cityname

## Response

REST API with Json response
looks like this
```json
{
    "check": true,
    "criteria": {
        "daytemp": false,
        "naming": true,
        "rival": true
    }
}
```