
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
q=int(input())
for i in range(q):
    line2=input().split()
    a = line2[0]
    b = [line2[1]] #так как функция поиска предков работает по спискам, то вводимый в нее параметр тоже должен быть списком, иначе если он будет строкой, перебор пойдет посимвольно
    if (a in predki(b) or [a] == b) and a in catalog:  #защита от запроса является ли А предком А (конечно да) и от запроса о классах, не заявленных в первой части ввода.
        print('Yes')
    else: print("No")
    spisok_predkov = [] # когда запрос обработан, для работоспособности функции список предков обнуляем.