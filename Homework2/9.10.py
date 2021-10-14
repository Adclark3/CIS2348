# Avery Clark
# 1907691
import csv
number = {}
filename = input()

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line = next(csv_reader)
    for word in line:
        if word in number:
            number[word] += 1
        else:
            number[word] = 1


for i in number:
    print(i, number[i])
