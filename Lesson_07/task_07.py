import csv

header = ('name', 'surname', 'age')
name = input("Name: ").strip()
surname = input("Surname: ").strip()
age = input("Age: ").strip()
data = [name, surname, age]

with open('file_07.txt', 'w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    writer.writerow(header)
    writer.writerow(data)
