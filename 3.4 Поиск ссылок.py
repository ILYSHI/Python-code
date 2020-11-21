import requests
import re

link1 = input().rstrip()
link2 = input().rstrip()

res = requests.get(link1)
content = res.text
pattern = r'<a href="(.*html)'
link = re.findall(pattern,content)
lst = []
for i in link:
    res = requests.get(i)
    content = res.text
    links = re.findall(pattern, content)
    for j in links:
        lst.append(j)
if link2 in lst:
    print('Yes')
else:
    print('No')

