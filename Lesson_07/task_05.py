import json

with open('file_04.txt', 'r') as file:
    data = json.load(file)
    print('{name} {surname} {age}'.format(**data))

