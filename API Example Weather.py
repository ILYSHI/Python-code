import requests

city = input('City? ')
api_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    "q":city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units':'metric'
}

res = requests.get(api_url, params=params)
data = res.json()
template = 'Температура в {} {} градусов'
print(template.format(city,data['main']['temp']))