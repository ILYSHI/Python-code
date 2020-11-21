import os
import os.path
os.chdir('get')
a=[]
for current_dir, dirs, files in os.walk('main'):
    for i in files:
        if i[-3:]=='.py':
            if current_dir not in a:
                a.append(current_dir)
with open ('ans2.txt','w') as out:
    for i in a:
        out.write(i)
        out.write('\n')