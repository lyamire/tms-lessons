import json

data = {'name': 'Tatsiana', 'surname': 'Maiseyeva', 'age': '29'}

with open('file_03.json', 'w') as file:
    json.dump(data, file)

