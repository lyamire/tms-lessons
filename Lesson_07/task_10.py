import openpyxl

name, surname, age = map(str, input('Enter your first name, surname and age separated by a space: ').split())

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Age'
sheet['A2'] = name
sheet['B2'] = surname
sheet['C2'] = age

wb.save('file_10.xlsx')
