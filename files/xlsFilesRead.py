#!/usr/bin/python3
import xlrd
# import numpy as np
import matplotlib.pyplot as plt

wb = xlrd.open_workbook('Variflight_MU5735_20220321.xls')
dataSheet = wb.sheets()[0]
dataLongi = list(map(float, dataSheet.col_values(7, 1, dataSheet.nrows)))
dataLat = list(map(float, dataSheet.col_values(8, 1, dataSheet.nrows)))

print(dataLongi, type(dataLongi[0]), dataLat, type(dataLat[0]))

plt.figure(1, dpi=100)
plt.plot(dataLongi, dataLat, c='green')
plt.xlabel('Longitude',fontsize=14)
plt.ylabel('Latitude',fontsize=14)
plt.xlim(min(dataLongi), max(dataLongi))
plt.ylim(min(dataLat), max(dataLat))
# plt.tick_params(axis='both',which='major',labelsize=14)

# print(range(min(dataLongi), max(dataLongi), 0.1))

# plt.xticks(range(min(dataLongi), max(dataLongi), 0.1))
# plt.yticks(range(min(dataLat), max(dataLat), 0.1))
plt.show()

print(dataLongi, dataLat, min(dataLongi), max(dataLongi), '\n')




wb = xlrd.open_workbook(r"QFII重仓流通股.xls")
sheet_name = wb.sheet_names()[0]
sheet = wb.sheet_by_index(0)                                # sheet索引从0开始
print (wb.nsheets, sheet.name, sheet.nrows, sheet.ncols, '\n')

rows = sheet.row_values(1)                                  # 获取第2行内容
cols = sheet.col_values(0)                                  # 获取第1列内容
# print (rows, cols)




wb = xlrd.open_workbook('乘法表.xls')
ws = wb.sheets()
print(ws)
wsname = wb.sheet_names()
print(type(wsname), len(wsname), wsname)
ws1 = wb.sheet_by_name('Sheet1')
ws2 = wb.sheet_by_index(1)
ws3 = wb.sheets()[1]
print(ws1, ws2, ws3)