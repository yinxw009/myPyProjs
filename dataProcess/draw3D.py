#!/usr/bin/python3
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D





fig1 = plt.figure(1, dpi=120)                               #创建图表1，dpi为设置图表的大小，默认dpi=80

ax4 = fig1.add_subplot(224, projection='3d')                # 图4散点图
xx = np.random.random(20)*10-5                              #取100个随机数，范围在5~5之间
yy = np.random.random(20)*10-5
X, Y = np.meshgrid(xx, yy)
Z = np.sin(np.sqrt(X**2+Y**2))
ax4.scatter(X,Y,Z,alpha=0.3,c=np.random.random(400),s=np.random.randint(10,20, size=(20, 40)))     #生成散点.利用c控制颜色序列,s控制大小





ax3 = fig1.add_subplot(223, projection='3d')  # 图3等高线
xx = np.arange(-5,5,0.1)
yy = np.arange(-5,5,0.1)
X, Y = np.meshgrid(xx, yy)
Z = np.sin(np.sqrt(X**2+Y**2))
ax3.plot_surface(X,Y,Z,alpha=0.3,cmap='winter')     #生成表面， alpha 用于控制透明度
ax3.contour(X,Y,Z,zdir='z', offset=-3,cmap="rainbow")  #生成z方向投影，投到x-y平面
ax3.contour(X,Y,Z,zdir='x', offset=-6,cmap="rainbow")  #生成x方向投影，投到y-z平面
ax3.contour(X,Y,Z,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影，投到x-z平面
#ax3.contourf(X,Y,Z,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影填充，投到x-z平面，contourf()函数




ax2 = fig1.add_subplot(222, projection='3d')  # 图2三维曲面
xx = np.arange(-5,5,0.5)
yy = np.arange(-5,5,0.5)
X, Y = np.meshgrid(xx, yy)
Z = np.sin(X)+np.cos(Y)
ax2.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap='rainbow')



# ax1 = plt.axes(projection='3d')
ax1 = fig1.add_subplot(221, projection='3d')  #画多个子图, 图1三维曲线和散点
z = np.linspace(0, 13, 1000)                 # x轴的定义域为0~13，中间间隔1000个元素
x = 5*np.sin(z)
y = 5*np.cos(z)
zd = 13*np.random.random(100)
xd = 5*np.sin(zd)
yd = 5*np.cos(zd)
ax1.scatter3D(xd,yd,zd, cmap='Blues')  #绘制散点图
ax1.plot3D(x,y,z,'gray')    #绘制空间曲线




plt.show()                                        #显示所有图表