import requests
import re

link1 = input().rstrip()
res = requests.get(link1)
content = res.text
lst=[]
#pattern = r"<a href=.(http|ftp)?s?(://)?(\w+.\w+\.?(\w+)?\.?(\w+)?).*>"
pattern = r"<a.*href=.(http|ftp)?s?(://)?([a-zA-Z0-9-_.]+\.\w+)(.*)>"
link = re.findall(pattern,content)
for i in link:
    lst.append(i[2])
a = sorted(set(lst))
print(*sorted(set(lst)),sep="\n")
