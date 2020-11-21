import json
'''
a = input()
inp_json = json.loads(a)
'''
inp_json = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
inp_json = [{"name": "G", "parents": ["ZZZ"]}, {"name": "TH", "parents": ["ZZZ"]}, {"name": "G", "parents": ["ZY"]}, {"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]
inp_json = [  # тестовый граф наследования в виде json-объекта
    {'name': 'G', 'parents': ['F']},  # сначала отнаследуем от F, потом его объявим: корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    {'name': 'A', 'parents': []},
    {'name': 'B', 'parents': ['A']},
    {'name': 'C', 'parents': ['A']},
    {'name': 'D', 'parents': ['B', 'C']},
    {'name': 'E', 'parents': ['D']},
    {'name': 'F', 'parents': ['D']},
    # а теперь другая ветка наследования
    {'name': 'X', 'parents': []},
    {'name': 'Y', 'parents': ['X', 'A']},  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    {'name': 'Z', 'parents': ['X']},
    {'name': 'V', 'parents': ['Z', 'Y']},
    {'name': 'W', 'parents': ['V']},
]


# Функция обработки списка словарей, преобразует словарь по имени ключ значение
dict = {}
for i in inp_json:
    dict[i['name']] = [i['name']]
    for j in i['parents']:
        dict[j] = [j]

def search(dict):
    for name in dict:
        unsorted = []
        unsorted += dict[name]
        while unsorted:
            name1 = unsorted.pop()
            for i in inp_json:
                if name1 in i['parents']:
                    dict[name].append(i['name'])
                    unsorted+=i['name']
search(dict)

for i in sorted(dict.keys()):
    print(i,':',len(set(dict[i])))
