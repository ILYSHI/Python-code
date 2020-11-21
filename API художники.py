import requests
import json

client_id = '366a61915e11c49e7fec'
client_secret = '8813f314913ab7ab872a835a3e6a76ec'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)
# разбираем ответ сервера
j = json.loads(r.text)


dict = {}
lines =  open('text.txt','r').readlines()
for i in lines:
        i = i.rstrip()
        url = 'https://api.artsy.net/api/artists/'+i
        r = requests.get(url, headers=headers )
        j = json.loads(r.text)
        birth = j['birthday']
        if birth not in dict:
            dict[birth] = [j['sortable_name']]
        else:
            dict[birth].append(j['sortable_name'])
print(dict)

for i in sorted(dict.keys()):
    print(*sorted(dict[i]),sep='\n')
