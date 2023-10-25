import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Gender'

sheet['A2'] = 'Tatsiana'
sheet['B2'] = 'Maiseyeva'
sheet['C2'] = 'Female'

wb.save('file_09.xlsx')
