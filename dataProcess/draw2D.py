#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np


plt.figure(4, dpi=100)                                                #创建图表4
locData = np.loadtxt('dataGGAconverted.txt', delimiter=',')           #加载数据文件，数据间的分隔符为逗号'，'
plt.plot(locData[:,2], locData[:,1], 'ro')                            #ro表示每个数据在图表上打印的是红色的圆点




plt.figure(3, dpi=100)                            #创建图表3

plt.subplot(221)                                  #创建2*2的图表矩阵，绘制的子图为矩阵中的1序号
x = np.linspace(-np.pi*2,np.pi*2,100)             #定义域为： -2pi 到 2pi 
for i in range(1,5):                              #画四条线
  plt.plot(x,np.sin(x/i), label="sin(x/i)")
plt.xlabel("X axe")                               #设置X轴的文字
plt.ylabel("Y axe")                               #设置Y轴的文字
plt.title("sin(x/i) function")                    #设置图的标题
# plt.legend()                                    #显示图例。 

plt.subplot(222)                                  # 绘制的子图为矩阵中的2序号
data = np.loadtxt('1.txt',delimiter=',')          #加载数据文件1.txt，数据间的分隔符为逗号'，'
plt.plot(data[:,0],data[:,1],'ro')                #ro表示每个数据在图表上打印的是红色的圆点





plt.figure(2, dpi=80)                             #创建图表2
ax1 = plt.subplot(211)                            #创建子图 ax1
ax2 = plt.subplot(212)                            #创建子图 ax2
 
x = np.linspace(0,10,100)                         # x轴定义域
 
plt.sca(ax1)                                      #选择子图ax1
plt.plot(x,np.exp(x))                             #在子图ax1 中绘制函数 exp(x) 
plt.sca(ax2)                                      #选择子图ax2
plt.plot(x,np.sin(x))                               #在子图ax2 中绘制函数 sin(x)




plt.figure(1, dpi=100)                            #创建图表1，dpi为设置图表的大小，默认dpi=80

plt.subplot(221)                                  #创建2*2的图表矩阵，绘制的子图为矩阵中的1序号
x = np.linspace(-np.pi,np.pi,100)                 # x轴的定义域为 -3.14~3.14，中间间隔100个元素
plt.plot(x,np.sin(x))


plt.subplot(222)                                  # 绘制的子图为矩阵中的2序号
data = [1,1,1,2,2,2,3,3,4,5,5,6,4]
plt.hist(data)                                    #只要传入数据，直方图就会统计数据出现的次数


plt.subplot(223)                                  # 绘制的子图为矩阵中的3序号
x = np.arange(1,10)  
y = x
plt.scatter(x, y, c = 'r', marker = 'o')             #c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形


plt.subplot(224)                                  # 绘制的子图为矩阵中的4序号
data = [100,500,300]                              # 饼图中的数据
plt.pie(data,                                     # 每个饼块的实际数据，如果大于1，会进行归一化，计算percentage
        explode=[0.0,0.0,0.1],                    # 每个饼块离中心的距离
        colors=['y','r','g'],                     # 每个饼块的颜色,黄红绿
        labels=['A part','B part','C part'],      # 每个饼块的标签
        labeldistance=1.2,                        # 每个饼块标签到中心的距离
        autopct='%1.1f%%',                        # 百分比的显示格式
        pctdistance=0.4,                          # 百分比到中心的距离
        shadow=True,                              # 每个饼块是否显示阴影
        startangle=0,                             # 默认从x轴正半轴逆时针起
        radius=1                                  # 饼块的半径
        )



plt.show()                                        #显示所有图表