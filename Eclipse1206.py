import numpy as np
import matplotlib.pyplot as plt

# 1.圆半径
r = 2.0
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
# 取圆上固定间隔的点，这里以40个点为例
for i in range(40):
    # x1,y1是椭圆位于圆上的焦点
    x1 = xx[i*15]
    y1 = yy[i*15]

    # 定义两焦点间距为c1 = 5.0
    c1 = 5.0
    # 定义长轴长c = 8
    c = 8
    # 经过运算得到圆外另一焦点的坐标
    x2 = (c1 + r) * x1 / r
    y2 = (c1 + r) * y1 / r

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



