import csv

header = ('name', 'surname', 'gender')
data = ['Tatsiana', 'Maiseyeva', 'F']

with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    writer.writerow(header)
    writer.writerow(data)

