import re
a = 'Beautiful is better than ugly. Explicit is better than implicit.'
pattern = r'\b[a-zA-Z.]+'
lst = re.findall(pattern,a)
print(lst)
dict = {}
for i in lst:
    if len(i) not in dict:
        dict[len(i)] = 1
    else:
        dict[len(i)]+=1
for i in sorted(dict.keys()):
    print(i,': ',dict[i],sep='')
