import requests
import csv
url = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_16/sitka_weather_07-2014.csv'
data = requests.get(url)
print(data.headers['Content-Type'])

with open('sitka_weather.csv','w') as out:
    out.write(data.text)
