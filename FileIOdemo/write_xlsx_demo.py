from faker import Faker
from openpyxl import Workbook

wb =Workbook()
ws = wb.active


row_count = 5
col_count = 4

for i in range (1,row_count+1):
    for j in range (1,col_count+1):
        ws.cell(row=i,column=j).value = i+j


wb.save("Demoexcel.xlsx")


