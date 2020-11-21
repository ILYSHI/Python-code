import requests
while True:
    number = input()
    url = 'http://numbersapi.com/'+number+'/math?json=true'
    res = requests.get(url)
    data = res.json()
    if data['found']:
        print('Interesting')
        print(data['text'])
    else:
        print('Boring')
