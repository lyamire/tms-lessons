import json

name, surname, age = map(str, input('Enter your first name, surname and age separated by a space: ').split())

data = {'name': name, 'surname': surname, 'age': age}


with open('file_04.txt', 'w') as file:
    json.dump(data, file)




