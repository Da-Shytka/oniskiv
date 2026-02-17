import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def integral(f, a, b, n):
    h = (b-a)/n
    total = 0.0
    for i in range(n):
        x_mid = a+(i+0.5)*h
        total+=f(x_mid)
    return total*h

A = 1
phi = 0
T = 50
w = 2*math.pi/T

a = []
tau = []

def s(t, A, w, phi):
    return A*math.sin(w*t+phi)+math.sin(2*math.pi/10*t)

def hat(a, tau, t):
    return (1/math.sqrt(a))*(1-((t-tau)/a)**2)*math.exp(-0.5*((t-tau)/a)**2)

tau_values = range(0, 51)
a_values = range(1, 31)

W_s = np.zeros((len(a_values), len(tau_values)))

for i, a in enumerate(a_values):
    for j, tau in enumerate(tau_values):
        def integrand(t, a=a, tau=tau):
            return s(t, A, w, phi) * hat(a, tau, t)
        W_s[i, j] = integral(integrand, -25, 75, 1000)

# plt.figure()
# plt.imshow(
#     W_s,
#     cmap='gray',
#     aspect='auto',
#     origin='lower',
#     extent=[min(tau_values), max(tau_values), min(a_values), max(a_values)]
# )
# plt.colorbar()
# plt.xlabel('tau')
# plt.ylabel('a')
# plt.show()

TAU, A_grid = np.meshgrid(tau_values, a_values)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    TAU,
    A_grid,
    W_s,
    cmap='gray',
    linewidth=0,
    antialiased=True
)

ax.set_xlabel('tau')
ax.set_ylabel('a')
ax.set_zlabel('W_s')
plt.show()

   