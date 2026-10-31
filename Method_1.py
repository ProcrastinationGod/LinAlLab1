from unittest import case
import numpy as np
# Вершины тетраэдра
A = np.array([0, 0, 0])
B = np.array([2, 0, 0])
C = np.array([0, 2, 0])
D = np.array([0, 0, 2])

#Тестовые точки
points = {
 	"P1": [0.5, 0.5, 0.5],
    "P2": [0.5, 0.5, 0],
 	"P3": [1, 0, 0],
 	"P4": [0, 0, 0],
 	"P5": [3, 3, 3]
 }

#Вычисление объема тетраэдра
def v_tetr(a, b, c, d):
    matrix = np.array([a - d, b - d, c - d])
    return abs(np.linalg.det(matrix)) / 6

#Проверяем принадлежность точки
def check(a, b, c, d, p):
    v = v_tetr(a, b, c, d)
    v1 = abs(v_tetr(p, b, c, d))
    v2 = abs(v_tetr(a, p, c, d))
    v3 = abs(v_tetr(a, b, p, d))
    v4 = abs(v_tetr(a, b, c, p))
    v_zeros = [v1, v2, v3, v4].count(0)
    eps = 1e-9
    if abs(v - (v1 + v2 + v3 + v4)) > eps: return "Снаружи"
    elif abs(v - (v1 + v2 + v3 + v4)) < eps:
        match v_zeros:
            case 0: return "Внутри"
            case 1: return "На грани"
            case 2: return "На ребре"
            case 3: return "Совпадает с вершиной"

for name, p in points.items():
   print(f'Точка {name} {check(A, B, C, D, p)} тетраэдра')
