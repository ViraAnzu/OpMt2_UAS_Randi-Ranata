import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Particle Swarm Optimization - Studi Kasus Sederhana")
st.write("Mencari posisi optimal dengan biaya minimum")

target = st.slider("Target lokasi (a)", -20, 20, 5)
n_particles = st.slider("Jumlah partikel", 5, 30, 10)
n_iter = st.slider("Jumlah iterasi", 1, 50, 10)

def fitness(x, a):
    return (x - a) ** 2

w = 0.5
c1 = 1.5
c2 = 1.5

x = np.random.uniform(-20, 20, n_particles)
v = np.zeros(n_particles)

pbest_x = x.copy()
pbest_f = fitness(x, target)

gbest_x = pbest_x[np.argmin(pbest_f)]
gbest_f = np.min(pbest_f)

history = []

for _ in range(n_iter):
    r1 = np.random.rand(n_particles)
    r2 = np.random.rand(n_particles)

    v = (
        w * v
        + c1 * r1 * (pbest_x - x)
        + c2 * r2 * (gbest_x - x)
    )

    x = x + v
    fx = fitness(x, target)

    for i in range(n_particles):
        if fx[i] < pbest_f[i]:
            pbest_x[i] = x[i]
            pbest_f[i] = fx[i]

    gbest_x = pbest_x[np.argmin(pbest_f)]
    gbest_f = np.min(pbest_f)

    history.append(gbest_x)

st.subheader("Hasil Optimasi")
st.write(f"Posisi optimal ditemukan: **{gbest_x:.4f}**")
st.write(f"Nilai biaya minimum: **{gbest_f:.4f}**")

fig, ax = plt.subplots()

ax.plot(history, marker="o")
ax.axhline(target, linestyle="--")
ax.set_xlabel("Iterasi")
ax.set_ylabel("Posisi gBest")
ax.set_title("Pergerakan gBest menuju target")

st.pyplot(fig)