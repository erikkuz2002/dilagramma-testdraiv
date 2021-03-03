import matplotlib.pyplot as plt
import numpy as np

#Формирование данных X и построение линии Y
#-13 -12 -11 -10 -9 -8-7-6-5-4-3-2-1 0 1 2 3 4 5 6 7 8 9 10 11 12 13
x1 = np.arange(-9, 0)#red
y1 = -1/8*(x1+9)**2+8
x2 = np.arange(1, 10)#red
y2 = -1/8*(x2-9)**2+8
x3 = np.arange(-9, -7)#blue
y3 = 7*(x3+8)**2+1
x4 = np.arange(8, 10)#oganze
y4= 7*(x4-8)**2+1
x5 = np.arange(-8, 0)
y5= 1/49*(x5+1)**2
x6 = np.arange(1, 9)#
y6= 1/49*(x6-1)**2
x7 = np.arange(-8, 0)
y7= -4/49*(x7+1)**2
x8 = np.arange(1, 9)
y8= -4/49*(x8-1)**2
x9 = np.arange(-8, -1)
y9= 1/3*(x9+5)**2-7
x10 = np.arange(2, 9)
y10= 1/3*(x10-5)**2-7
x11 = np.arange(-2, 0)
y11= -2*(x11+1)**2-2
x12 = np.arange(1, 3)
y12= -2*(x12-1)**2-2#!
x13 = np.arange(-1, 1.1,0.1)
y13= -4*x13**2+2
x14 = np.arange(-1, 1.1,0.1)
y14= 4*x14**2-6
x15 = np.arange(-1, 0,0.1)
y15= -1.5*x15+2
x16 = np.arange(0, 2)
y16= 1.5*x16+2

plt.subplots()
plt.title("бабочка") #название графика
plt.plot(x1,y1,'r',x2,y2,'r',x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16,linewidth=5)# График красного цвета

plt.savefig("my_image.png") # Сохранение изображения или
plt.show() # Вывод изображения на экран

fail=open("dannie.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()

plt.title("Данные о ИТ безопасности")
plt.grid(True)

color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)

plt.show()


fail=open("text_num2.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()

plt.title("vvv1")
plt.grid(True)

color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)

plt.show()

fail=open("text_num3.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()
print(mas2)
plt.title("vvv2")
plt.grid(True)

plt.pie(mas2,labels=mas1,autopct="%.1f%%", radius=1) # кругавая дилаграмма
plt.show()

fail=open("text_num1.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()

plt.grid(True)
plt.title("заражение то короновирусом")
plt.pie(mas2,labels=mas1,autopct="%.1f%%",radius=1) # кругавая дилаграмма
plt.show()