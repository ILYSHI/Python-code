import json

inp_json = json.loads(input())

# Функция обработки списка словарей, преобразует словарь по имени ключ значение

def sorter(sp_sl):
    dict = {}
    for i in sp_sl:
        key = i['name']
        value = i['parents']
        dict[key] = value
    return dict
# print(inp_json)
parents = sorter(inp_json)
potomki = {}
for i in parents:
    for j in parents[i]:
        if j not in potomki:
            potomki[j]=[i]
        else:
            potomki[j].append(i)

lst = []
def childs(predok):
    if predok in potomki:
        for i in potomki[predok]:
            lst.append(i)
            childs(i)
    return(len(set(lst))+1)


for i in sorted(parents.keys()):
    lst = []
    number = childs(i)
    print(i,':',number)
