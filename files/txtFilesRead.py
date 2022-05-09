#!/usr/bin/python3
fo = open('note.txt',"r+")
print("File name is : ",fo.name)
for lines in fo.readlines():
  print("Read line is : ",lines)
fo.close


fo = open('note.txt',"r+")
line = fo.readline()
print("First line is : ",line,"Second line is : ",fo.readline())
fo.close


fo = open('note.txt',"r+")
str = fo.read(27)
print("File name is : ",fo.name)
print("Read String is : ",str)
fo.close


fo = open("note.txt", "w")
print( "文件名 : ", fo.name)
print( "是否已关闭 : ", fo.closed)
print( "访问模式 : ", fo.mode)
# print( "末尾是否强制加空格 : ", fo.softspace)
fo.close