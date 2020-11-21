import csv
dict = {}
Russia = {}
with open('covid.csv','r') as inf:
    data = csv.reader(inf)
    for row in data:
        if row[0] != 'FIPS':
            if row[3] not in dict:
                dict[row[3]] = int(row[7])
            else:
                dict[row[3]]+= int(row[7])
        if row[3] == 'Russia':
            Russia[row[2]] = int(row[7])
# for i in dict:
    # print(i,dict[i])

list_d = list(Russia.items())
list_d.sort(key=lambda i: i[1],reverse=True)
for reg, num in list_d:
    print(reg,'-',num,'Номер в рейнтинге:',list_d.index((reg,num))+1)