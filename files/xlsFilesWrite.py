import xlrd

wb = xlrd.open_workbook('乘法表.xls')
ws = wb.sheets()
print(ws)
wsname = wb.sheet_names()
# print(wsname)
ws1 = wb.sheet_by_names()
ws2 = wb.sheet_by_index(1)
ws3 = wb.sheets()[1]