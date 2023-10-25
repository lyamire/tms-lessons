import csv

header = ('name', 'surname', 'age')
name = input("Name: ")
surname = input("Surname: ")
age = input("Age: ")
data = [name, surname, age]

with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    writer.writerow(header)
    writer.writerow(data)
