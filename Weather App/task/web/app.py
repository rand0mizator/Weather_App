from flask import Flask
from flask import render_template, request
import requests

import sys

API_KEY = '7dcc958267a403d0d0c48ce4f39a01be'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET, POST'])
def add_city():
    city_name = request.form['input_city']
    return city_name


def get_weather(city_name):
    weather = requests.get(f'api.openweathermap.org/data/2.5/forecast?id={city_name}&appid={API_KEY}')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()


import requests
import json


city = 'Tomsk'
API_KEY = '7dcc958267a403d0d0c48ce4f39a01be'


def get_weather(city_name):
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}')
    weather_json = json.loads(weather.text)
    weather_type = json.dumps(weather_json['weather'][0]['main'])
    temperature = json.dumps(weather_json['main']['temp'])

    print(weather_type, temperature, city_name)


get_weather(city)

