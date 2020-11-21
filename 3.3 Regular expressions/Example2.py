import re
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


pattern = r'a.c'
string = "acc"
match = re.search(pattern,string)
print(match)

string = "abc, a.c, a0c, aNc, aacc"
all_inclusions = re.findall(pattern,string)
print(all_inclusions)