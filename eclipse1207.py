import numpy as np
import matplotlib.pyplot as plt

# 1.圆半径
r = input("Input radius or the circle: r = ")
r = float(r)
# 2.圆心坐标
a0, b0 = 0., 0.

theta = np.arange(0, 2 * np.pi, 0.01)
xx = a0 + r * np.cos(theta)
yy = b0 + r * np.sin(theta)

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(xx, yy)

axes.axis('equal')

# 3. 开始画椭圆族
# 取圆上固定间隔的点，个点为例
total_count = len(xx)

n = input("How many ellipse you want?")
n = int(n)

for i in range(n):
    # 挑选椭圆位于圆上的焦点I
    x1 = input("Please choose x Position of the focii I (|x1| <= r) : x1 = ")
    x1 = float(x1)
    y1 = np.sqrt(r ** 2 - x1 ** 2)

    choice1 = input("Input 1 if you want y Position of the focii I y1 >0\n else input 0:")
    if int(choice1) == 1:
        y1 = float(y1)
    else:
        y1 = -float(y1)
    # 挑选椭圆位于圆上的焦点II
    x2 = input("Please choose x Position of the focii I (|x2| <= r) : x2 = ")
    x2 = float(x2)
    y2 = np.sqrt(r ** 2 - x2 ** 2)

    choice1 = input("Input 1 if you want y Position of the focii I y1 >0\n else input 0:")
    if int(choice1) == 1:
        y2 = float(y2)
    else:
        y2 = -float(y2)

    # 定义长轴长c
    c = input("Input major axis: c = ")
    c = float(c)
    if c < np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2):
        print("c is not long enough, please input again!")
        c = input("Input major axis: c = ")
        c = float(c)

    # Compute ellipse parameters
    a = c / 2  # Semimajor axis
    x0 = (x1 + x2) / 2  # Center x-value
    y0 = (y1 + y2) / 2  # Center y-value
    f = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)  # Distance from center to focus
    b = np.sqrt(a ** 2 - f ** 2)  # Semiminor axis
    phi = np.arctan2((y2 - y1), (x2 - x1))  # Angle betw major axis and x-axis

    # Parametric plot in t
    resolution = 1000
    t = np.linspace(0, 2 * np.pi, 1000)
    x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
    y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)

    # Plot ellipse
    plt.plot(x, y)

    # Show focii
    plt.plot(x1, y1, 'bo')
    plt.plot(x2, y2, 'bo')
    plt.plot((x1, x2), (y1, y2))

    plt.axis('equal')
plt.show()