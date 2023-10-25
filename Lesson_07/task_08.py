import csv

with open('file_07.txt', 'r') as file:
    file_reader = csv.reader(file, delimiter=',')
    next(file_reader)
    for row in file_reader:
        print(f'{row[1]} {row[0]} {row[2]}')
