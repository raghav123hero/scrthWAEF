
import math
import csv

with open('data.csv', newline='') as rag:
    reader = csv.reader(rag)
    fileData = list(reader)


data = fileData[0]

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

square= []
for number in data:
    a = int(number) - mean(data)
    a= a**2

sum =0
for i in square:
    sum =sum + i

answer = sum/ (len(data)-1)

std = math.sqrt(answer)
print(std)

