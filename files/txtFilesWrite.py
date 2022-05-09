#!/usr/bin/python3
fo = open('note.txt',"w+")
len = fo.write( "Python is a great language.\nYeah, its great!!\n")
print("Writed length = ",len,"\n",fo.read,"\n")
fo.close


fo = open("note.txt", "w")
print( "文件名 : ", fo.name)
print( "是否已关闭 : ", fo.closed)
print( "访问模式 : ", fo.mode)
# print( "末尾是否强制加空格 : ", fo.softspace)
fo.close


