import numpy as np

# Функция которая возвращает уравнение плоскости по 3 точкам 
def plane_equation(p1, p2, p3):
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)
    normal = np.cross(v1, v2)
    A, B, C = normal
    f = lambda p: A*p[0] + B*p[1] + C*p[2]
    D = -f(p1)
    return lambda p: A*p[0] + B*p[1] + C*p[2] + D

# Функция, которая проверят принадлежность точки к тетраэдру
def check_point_location(A, B, C, D, P):
    # Список граней (Первые 3 элемента вершины грани, 4ый элемент противолежащая вершина)
    faces = [
        (A, B, C, D),
        (A, B, D, C),
        (A, C, D, B),
        (B, C, D, A)
    ]

    # Счетчик нулей
    zero_count = 0
    
    for v1, v2, v3, opp in faces:
        f = plane_equation(v1, v2, v3)
        val_opp = f(opp)
        val_p = f(P)

        # Произведение дает положительный результат (то есть знак одинаковый), если противолеж. вершина и произвольная точка лежат по 1 сторону от грани
        # Если произведение равно 0, а это только про val_p = 0, то значит точка принадлежит грани
        product = val_p * val_opp

        # Если произведение меньше 0, то знаки значений разные и вершина и точка лежат по разные стороны, значит точка снаружи тетраэдра
        if product < 0:
            return "Снаружи"
        elif product == 0: # Увеличиваем счетчик, если произведение равно 0
            zero_count += 1

    if zero_count == 0:
        return "Строго внутри"
    elif zero_count == 1:
        return "На грани"
    elif zero_count == 2:
        return "На ребре"
    return "Совпадение с вершиной"

# Наши точки A, B, C, D
A, B, C, D = [0, 0, 0], [2, 0, 0], [0, 2, 0], [0, 0, 2]
# Точки в пространстве которые мы проверяем
P_list = [[0.5, 0.5, 0.5], [0.5, 0.5, 0], [1, 0, 0], [0, 0, 0], [3, 3, 3]]

for P in P_list:
    print("P :", P, ".""Результат:", check_point_location(A, B, C, D, P))