import pytest
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import weather
load_dotenv()
dotenv_path = Path('.env')

url = 'http://127.0.0.1:5000'


def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200

def test_check_nocity_errorhandler():
    r = requests.get(url + '/check/')
    assert r.status_code == 404

def test_check_city():
    r = requests.get(url + '/check?city=oslo')
    assert r.status_code == 200

def test_check_mispelledcity():
    r = requests.get(url + '/check?city=londun')
    assert r.status_code == 500

def test_unit_test_main():
    r = weather.main('London')
    assert r['check'] == True
