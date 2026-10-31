import numpy as np

def classify_point_barycentric(P, A, B, C, D, tol=1e-7):
    # Матрица перехода: [B-A, C-A, D-A]
    T = np.column_stack([np.array(B) - np.array(A), 
                         np.array(C) - np.array(A), 
                         np.array(D) - np.array(A)])
    
    # Вектор смещения P - A
    v = np.array(P) - np.array(A)
    
    # Вычисление beta, gamma, delta
    beta, gamma, delta = np.linalg.solve(T, v)
    alpha = 1.0 - (beta + gamma + delta)
    coords = np.array([alpha, beta, gamma, delta])
    
    # Применение порога погрешности tol
    coords[np.abs(coords) < tol] = 0.0
    
    # Классификация
    if np.any(coords < 0.0):
        return "Снаружи", coords
    
    zero_count = np.count_nonzero(coords == 0.0)
    if zero_count == 0:
        return "Внутри тетраэдра", coords
    elif zero_count == 1:
        return "На грани", coords
    elif zero_count == 2:
        return "На ребре", coords
    else:
        return "В вершине", coords

# Вершины
A, B, C, D = (0, 0, 0), (2, 0, 0), (0, 2, 0), (0, 0, 2)

# Проверка тестовых точек
test_points = [
    (0.5, 0.5, 0.5),
    (0.5, 0.5, 0),
    (1, 0, 0),
    (0, 0, 0),
    (3, 3, 3)
]

for pt in test_points:
    status, bary = classify_point_barycentric(pt, A, B, C, D)
    print(f"P{pt}: {status} (α={bary[0]:.2f}, β={bary[1]:.2f}, γ={bary[2]:.2f}, δ={bary[3]:.2f})")
