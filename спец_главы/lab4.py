import math
import matplotlib.pyplot as plt
import numpy as np

A = 3
c = []

def integral(f, a, b, n):
    h = (b-a)/n
    total = 0.0
    for i in range(n):
        x_mid = a+(i+0.5)*h
        total+=f(x_mid)
    return total*h

def funk(t):
    if t >= 0 and t <= 1:
        return A*(math.sin(math.pi*t))**2
    else: return 0

def h_0(t):
    if t >= 0 and t < 1: return 1
    else: return 0

def h_1(t):
    if t >= 0 and t < 1/2: return 1
    elif t >= 1/2 and t < 1: return -1
    else: return 0

c_0 = integral(funk, 0, 1, 1000)
c.append(c_0)
print("c_0", c_0)

c_1 = integral(funk, 0, 1/2, 1000) - integral(funk, 1/2, 1, 1000)
c.append(c_1)
print("c_1", c_1)

c_2 = math.sqrt(2)*(integral(funk, 0, 1/4, 1000) - integral(funk, 1/4, 1/2, 1000))
c.append(c_2)
print("c_2", c_2)

c_3 = math.sqrt(2)*(integral(funk, 1/2, 3/4, 1000) - integral(funk, 3/4, 1, 1000))
c.append(c_3)
print("c_3", c_3)

c_4 = 2*(integral(funk, 0, 1/8, 1000) - integral(funk, 1/8, 1/4, 1000))
c.append(c_4)
print("c_4", c_4)

c_5 = 2*(integral(funk, 1/4, 3/8, 1000) - integral(funk, 3/8, 1/2, 1000))
c.append(c_5)
print("c_5", c_5)

c_6 = 2*(integral(funk, 1/2, 5/8, 1000) - integral(funk, 5/8, 3/4, 1000))
c.append(c_6)
print("c_6", c_6)

c_7 = 2*(integral(funk, 3/4, 7/8, 1000) - integral(funk, 7/8, 1, 1000))
c.append(c_7)
print("c_7", c_7)

n_values = list(range(len(c)))
plt.figure()
plt.stem(n_values, c)
plt.xlabel("n")
plt.ylabel("c_n")
plt.title("Коэффициенты c_n")
plt.grid(True)
plt.show()

def x_star(t):
    return (h_0(t)*c_0
    + h_1(t)*c_1
    + math.sqrt(2)*h_1(2*t)*c_2
    + math.sqrt(2)*h_1(2*t - 1)*c_3
    + 2*h_1(4*t)*c_4
    + 2*h_1(4*t - 1)*c_5
    + 2*h_1(4*t - 2)*c_6
    + 2*h_1(4*t - 3)*c_7
    )

t_values = np.linspace(0, 1, 1000)
f_values = [funk(t) for t in t_values]
x_star_values = [x_star(t) for t in t_values]
plt.figure()
plt.plot(t_values, f_values, label='x(t)', color='blue')
plt.plot(t_values, x_star_values, label='x*(t)', color='red', linestyle='--')
plt.xlabel("t")
plt.ylabel("x*")
plt.title("Аппроксимация функции с использованием коэффициентов c_n")
plt.grid(True)
plt.legend()
plt.show()

different = [funk(t) - x_star(t) for t in t_values] 
plt.figure()
plt.plot(t_values, different, color='red')
plt.xlabel("t")
plt.ylabel("e(t)")
plt.grid(True)
plt.legend()
plt.show()

def integrate_trapezoid(values, time):
    total = 0.0
    for i in range(len(values) - 1):
        dx = time[i + 1] - time[i]
        height = ((values[i])**2 + (values[i + 1])**2) / 2.0
        total += height * dx
    return total

sigma = (integrate_trapezoid(different, t_values))
print(sigma)
