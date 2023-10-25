import csv

header = ('name', 'surname', 'gender')
data = [('Tatsiana', 'Maiseyeva', 'F')]

with open('file_06.txt', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerow(data)

