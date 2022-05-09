#!/usr/bin/python3
# -*- coding: utf-8 -*-
# source:gitee, https://gitee.com/Jclian91/24DianJiJiSuan
import itertools

#with brackets
def with_brackets(lst, ops_lst):                                                    #数值列表，运算符列表，
    for op in ops_lst:
        # expr0 =     lst[0]+op[0]+lst[1]+op[1]+lst[2]+op[2]+lst[3]                                                              #无括号时的运算情形
        expr1 = '('+lst[0]+op[0]+lst[1]+')'+op[1]+lst[2]+op[2]+lst[3]
        expr2 = '('+lst[0]+op[0]+lst[1]+op[1]+lst[2]+')'+op[2]+lst[3]
        expr3 = lst[0]+op[0]+'('+lst[1]+op[1]+lst[2]+')'+op[2]+lst[3]
        expr4 = '('+lst[0]+op[0]+lst[1]+')'+op[1]+'('+lst[2]+op[2]+lst[3]+')'
        
        for expr in [expr1, expr2, expr3, expr4]:
            try:
                t=eval(expr)
            except:                                                                 #作除法时，跳过分母为0时的情形
                pass
            
            if abs(t-24) < 0.001:                                                   #float型数值计算存在微小的误差
                return expr
    return 0

#返回4个数计算24的方法
def hasMethod(numbers, ops_lst):
    for lst in itertools.permutations(numbers):
        lst = list(map(lambda x:str(x), lst))
        #without brackets
        for op in ops_lst:
            expr = lst[0]+op[0]+lst[1]+op[1]+lst[2]+op[2]+lst[3]
            if abs(eval(expr)-24) < 0.001:
                return expr
        #with brackets
        expr = with_brackets(lst, ops_lst)
        if expr != 0:
            return expr
    
    return 0
        
#返回4个数计算24的方法，无方法时返回"No Method"
def cal_24(numbers):
    ops = ['+','-','*','/']
    ops_lst = [[i,j,k] for i in ops for j in ops for k in ops]
    
    expr = hasMethod(numbers, ops_lst)
    if expr != 0:
        return expr
    else:
        return 'No method!'

#所有情况的计算24点的办法，并输出到文本文件
def main():
    with open(r"D:\Projects\PyProjs\myProjs\my24pCal\24dian.txt",'r+') as proFile:
        numbers_lst = eval(proFile.read())  

    with open(r"D:\Projects\PyProjs\myProjs\my24pCal\24dian_ans.txt","w") as ansFile:
        for numbers in numbers_lst:
            strNum = list(map(lambda x: str(x), numbers))
            # print(type(numbers))
            ansFile.write("[%s,%s,%s,%s]: %s\n"%(strNum[0],strNum[1],strNum[2],strNum[3],cal_24(numbers)))

    inLst = list(eval(input("Please input numbers:")))
    print("[%s,%s,%s,%s]: %s\n"%(inLst[0],inLst[1],inLst[2],inLst[3],cal_24(inLst)))

main()
input('Press <Enter>')