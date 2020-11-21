import csv
import re
dict = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        pattern = r'.*\b../../(\d+)\b'
        match = re.match(pattern,str(row))
        if match != None:
            year = match.group(1)
            type_crime = row[5]
            if year == '2015':
                if type_crime not in dict:
                    dict[type_crime] = 1
                dict[type_crime]+=1
max_number = 0
for type_crime, number in dict.items():
    if max_number < number:
        max_number = number
        ans_type = type_crime
print(ans_type,max_number)




