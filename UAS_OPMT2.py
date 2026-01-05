import numpy as np
def fitness(x):
    return x**2 - 10*x + 25

w = 0.5
c1 = 1.5
c2 = 1.5
r1 = 0.5
r2 = 0.7

x = np.array([1, 8, 12, 3, 10], dtype=float)
v = np.array([0, 0, 0, 0, 0], dtype=float)

pbest_x = x.copy()
pbest_f = fitness(pbest_x)

gbest_index = np.argmin(pbest_f)
gbest_x = pbest_x[gbest_index]
gbest_f = pbest_f[gbest_index]

print("gBest awal:", gbest_x)
print("f(gBest):", gbest_f)

v = (
    w * v
    + c1 * r1 * (pbest_x - x)
    + c2 * r2 * (gbest_x - x)
)

x = x + v
fx = fitness(x)

for i in range(len(x)):
    if fx[i] < pbest_f[i]:
        pbest_x[i] = x[i]
        pbest_f[i] = fx[i]

gbest_index = np.argmin(pbest_f)
gbest_x = pbest_x[gbest_index]
gbest_f = pbest_f[gbest_index]

print("Setelah Iterasi 1")
print("x:", x)
print("f(x):", fx)
print("gBest:", gbest_x)
print("f(gBest):", gbest_f)

v = (
    w * v
    + c1 * r1 * (pbest_x - x)
    + c2 * r2 * (gbest_x - x)
)

x = x + v
fx = fitness(x)

for i in range(len(x)):
    if fx[i] < pbest_f[i]:
        pbest_x[i] = x[i]
        pbest_f[i] = fx[i]

gbest_index = np.argmin(pbest_f)
gbest_x = pbest_x[gbest_index]
gbest_f = pbest_f[gbest_index]

print("Setelah Iterasi 2")
print("x:", x)
print("f(x):", fx)
print("gBest:", gbest_x)
print("f(gBest):", gbest_f)