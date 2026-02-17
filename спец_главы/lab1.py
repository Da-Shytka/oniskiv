import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

n = 12
month = np.arange(1,13)
price = [6.1, 8.1, 9, 8.2, 7.8, 8, 8.2, 10, 11.3, 11, 10.2, 9.8]

# ========================
# А) оценить тренд 
# ========================

x_mean = sum(month) / n
y_mean = sum(price) / n

sum_x_y = 0
sum_x_2 = 0 # квадрат х
for i in range (0, n):
    sum_x_y += month[i] * price[i]
    sum_x_2 += month[i]**2

a = (1/n * sum_x_y - x_mean * y_mean)/(1/n * sum_x_2 - x_mean**2)
b = y_mean - a * x_mean

y_pred = []
for t in range (1, n+1):
    y_pred.append(a*t + b)

print("y = ", a,"*t + ", b)

# ========================
# В) периодическая составляющая
# ========================

delta = []
for i in range (0, n):
    delta.append(price[i]-y_pred[i])


# ========================
# С) разложение в ряд
# ========================

t = np.arange(1,13)
a1 = (1/6)*np.sum(delta*np.cos(t*math.pi/6))
a2 = (1/6)*np.sum(delta*np.cos(2*t*math.pi/6))
b1 = (1/6)*np.sum(delta*np.sin(t*math.pi/6))
b2 = (1/6)*np.sum(delta*np.sin(2*t*math.pi/6))

delta_t = a1*np.cos(t*np.pi/6) + a2*np.cos(2*t*np.pi/6) + b1*np.sin(t*np.pi/6) + b2*np.sin(2*t*np.pi/6)

print("\nКоэффициент а1: ", a1)
print("Коэффициент а2: ", a2)
print("Коэффициент b1: ", b1)
print("Коэффициент b2: ", b2)


# ========================
# Д) прогноз на 14 месяц
# ========================

delta_14 = (a1 * np.cos(14 * np.pi / 6)
        + a2 * np.cos(2 * 14 * np.pi / 6)
        + b1 * np.sin(14 * np.pi / 6)
        + b2 * np.sin(2 * 14 * np.pi / 6))

y_trend_14 = a * 14 + b
y_14 = y_trend_14 + delta_14

print("\nПрогноз на 14 месяц: ", y_14)

# ========================
# ГРАФИКИ
# ========================

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 2, figure=fig)

# -------- тренд ---------
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(month, y_pred, marker = 'o')
ax1.set_title("Тренд")
ax1.set_ylabel("Цена")
ax1.grid(True)

# -------- Переодическая составляющая (delta) ---------
ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(month, delta, marker = 'o')
ax2.set_title("Переодическая составляющая (delta)")
ax2.set_ylabel("Отклонение")
ax2.grid(True)

# -------- Апроксимация ---------
ax3 = fig.add_subplot(gs[0, 1])
ax3.plot(month, delta_t, marker = 'o')
ax3.set_title("Апроксимация")
ax3.set_xlabel("Месяц")
ax3.set_ylabel("Значение")
ax3.grid(True)

plt.tight_layout()
plt.show()