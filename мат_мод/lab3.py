import random
import math

w = [4, 6, 2, 8, 9, 1, 3, 5, 4, 3]
C = [5, 4.5, 6, 4, 3.5, 7, 4, 3, 6.5, 5.5]
finish_x = []
t = 10000
k = 0

def Yk(w, C, x):
    sum_Yk = 0
    for i in range (10):
        sum_Yk += w[i]*C[i]*x[i]
    return  sum_Yk

def limit(x, w):
    sum_limit = 0
    for i in range (10):
        sum_limit += w[i]*x[i]
    if sum_limit <= 32: return True
    else: return False

def random_x():
    return [random.randint(0, 1) for _ in range(10)]

def gibbs(y_delta, t):
    return math.exp(-y_delta / t)

x = random_x()
while not limit(x, w):
    x = random_x()

Y_pred = Yk(w, C, x)
print(x)

while (k != 10000):
    k += 1
    t = 100*0.1/k
    x = random_x()
    if limit(x, w):
        Y_prev = Yk(w, C, x)
        Y_delta = abs(Y_prev - Y_pred)
        if Y_prev > Y_pred:
            Y_pred = Y_prev
            finish_x = x
        else:
            r = random.random()
            if r < gibbs(Y_delta, t):
                Y_pred = Y_prev
                finish_x = x
            else:
                continue
    else: continue

print(finish_x)
P = 0
for i in range(10):
    P += w[i] * finish_x[i]
print(P)
print(Y_pred)