import csv
import math
with open('class1.csv',newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
filedata = []
for i in range (len(data)):
    nnum = data [i][1]
    filedata.append(float(nnum))

def mean(filedata):
    n = len(filedata)
    total = 0
    for x in filedata:
        total+=x

    mean = total/n
    return mean
squared_list=[]

for num in range (len(filedata)):
    a= int(num) - mean(filedata)
    a=a**2
    squared_list.append(a)
    
sum = 0
for i in squared_list:  
    sum= sum+i

result = sum/len(filedata)
standardDeviation = math.sqrt(result)

print(standardDeviation)

