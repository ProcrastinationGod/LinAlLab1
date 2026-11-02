import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Вершины тетраэдра
A = np.array([0, 0, 0])
B = np.array([2, 0, 0])
C = np.array([0, 2, 0])
D = np.array([0, 0, 2])

# Грани и противоположные вершины
faces = [
    (A, B, C, D),
    (A, D, B, C),
    (A, C, D, B),
    (B, D, C, A)
]

# Проверка принадлежности точки
def check(P):
    signs = []

    for X, Y, Z, Q in faces:
        n = np.cross(Y - X, Z - X)
        s = np.dot(n, P - X)
        t = np.dot(n, Q - X)
        signs.append((s, s * t))

    if any(p < -1e-9 for s, p in signs):
        return "Снаружи"
    elif any(abs(s) < 1e-9 for s, p in signs):
        return "На границе"
    else:
        return "Внутри"

# Тестовые точки из задания
points = {
    "P1": [0.5, 0.5, 0.5],
    "P2": [0.5, 0.5, 0],
    "P3": [1, 0, 0],
    "P4": [0, 0, 0],
    "P5": [3, 3, 3]
}

# Проверка точек
for name, p in points.items():
    print(name, check(np.array(p)))

# Построение тетраэдра
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

faces_plot = [
    [A, B, C], [A, B, D],
    [A, C, D], [B, C, D]
]

ax.add_collection3d(
    Poly3DCollection(faces_plot, alpha=0.2,
                     edgecolor="black")
)

# Отображение точек
for name, p in points.items():
    p = np.array(p)
    result = check(p)

    color = {
        "Внутри": "green",
        "Снаружи": "red",
        "На границе": "blue"
    }[result]

    ax.scatter(*p, color=color, s=50)
    ax.text(*p, name)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Тетраэдр и тестовые точки")

plt.show()
