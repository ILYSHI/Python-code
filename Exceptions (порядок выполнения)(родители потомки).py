
catalog={} #заводим каталог классов
n=int(input()) #вводим количество добавлений в каталог классов
for i in range(n):
    line = input().split()
    if len(line)==1: #Если символ один, заводим его в каталог со связью object (ноль в моем случае)
        catalog[line[0]]="0"
    else:
        index=line.index(":")+1 # Если выражение, разбираем по кусочкам, все что после двоеточия каталог родитель потомок
        for i in range(index,len(line)):
            if line[i] not in catalog: # для необъявленных классов добавляем их связь с object
                catalog[line[i]]="0"
            catalog[line[0]] = line[index:]
spisok_predkov=[]   #переменная поиска предков
def predki(a): #функция поиска предков для запращиваемого класса
    dlina=len(set(spisok_predkov)) #переменная длины, которая поможет остановить рекурсию, если новых предков не найдено
    for i in a:
        if i not in catalog: #если класс не объявлен, то и искать его нечего
            return []
        for j in catalog[i]: #если все же класс объявлен
            if j != "0": #и если его предок не object (т.к. это неинтересно, у них у всех предок object)
                spisok_predkov.append(j) #добавляем в список предков.
    if dlina<len(set(spisok_predkov)): #новый цикл рекурсии пройден, если новые предки найдены, то рекурсию продолжаем
        return predki(spisok_predkov)
    else:
        return set(spisok_predkov) #иначе выводим множество предков
func_del=[]
func_list=[]

q=int(input()) #вторая часть программы, вывод
for i in range(q):
    func=input() #вводим проверяемую функцию
    if func in func_list: #если она уже вводилась, в список удаления ее.
        func_del.append(func)
    for i in func_list: # для каждой ранее введенной функции
        if i in predki([func]) and func not in func_del: #проверяем нет ли родительских функций в списке уже введенных для данной функции, если есть - новую функцию в список удаления
            func_del.append(func)
    func_list.append(func) #добавляем вновь введеную функцию в общий список всех функций.
    spisok_predkov=[] #обнуляем список предков, чтобы проверять родителей следующей функции в цикле.
print(*func_del,sep="\n") #вывод списка накопленных ответов построчно.
