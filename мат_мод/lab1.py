import random
import math
import numpy as np

def func(x):
    return (1/3) * (x[0] + 1)**3 + x[1] - 2*x[0]*x[1] + x[2]**2

x_pred = [random.uniform(0, 10) for _ in range(3)]
temp = x_pred
N = 100              # число удачных шагов (k)
alpha = 0.1          # шаг
alpha_min = 0.0001     # минимальный шаг
x_prev = [0, 0, 0]

while np.abs(func(x_prev) - func(temp)) > 0.0000001:
    flag = False
    # print(alpha)
    # Генерация случайного направления
    ksi = [random.uniform(-1, 1) for _ in range(3)]
    norm = math.sqrt(sum(ksi[i]**2 for i in range(3)))

    # Новая точка
    for i in range(3):
        x_prev[i] = x_pred[i] + alpha * ksi[i] / norm
        x_prev[i] = max(0, min(10, x_prev[i]))
    
    if func(x_prev) > func(temp):
        temp = x_pred.copy()
        x_pred = x_prev.copy()
        flag = True
    else:
        for j in range(N):
            # Генерация случайного направления
            ksi = [random.uniform(-1, 1) for _ in range(3)]
            norm = math.sqrt(sum(ksi[i]**2 for i in range(3)))

            # Новая точка
            for i in range(3):
                x_prev[i] = x_pred[i] + alpha * ksi[i] / norm
                x_prev[i] = max(0, min(10, x_prev[i]))

            if func(x_prev) > func(temp):
                temp = x_pred.copy()
                x_pred = x_prev.copy()
                flag = True
                break

    if (flag == False):
        alpha *= 0.5
        print(f"alpha = {alpha}")
        if alpha < alpha_min:
            print(f"Достигнут минимальный шаг: {alpha_min}")
            break

print(f"Результат: {func(x_pred)}")
print(f"Точка: {x_pred}")