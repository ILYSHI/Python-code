import re
import sys
# print(re.search)
# print(re.findall)
# print(re.sub)
# [] - - множество подходящих символов
# . ^ $ * + ? {} [ ] \ | ( ) - - метасимволы
# \d ~ [0-9]
# \D ~ [^0-9]
# \s ~ [\t\n\r\f\v] - - пробельные символы
# \S ~ [^\t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] - - буквы + цифры + _
# \W ~ [^a-zA-Z0-9_] - - буквы + цифры + _
# b* - любое кол-во символов b [0...
# b? - кол-во b от [0,1]
# b+ - любое кол-во b от 1
# b{2,5} - кол-во b от 2 до 5 включая
# ((2)(3)) - группы, первая - общая, вторая (2) третья (3) для вызова \1 \2 \3 соотв.
# sub умеет заменять на группы r'\1' - каждый найденный match будет заменен на первую группу совпадения
for line in sys.stdin:
    line = line.rstrip()
    match = re.findall(r'[10][10]',(line+"0"))
    if (match.count('10')-match.count('01'))%3 == 0 and re.match(r'[10]+',line) and not re.search(r' ',line):
        print(line)