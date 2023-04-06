import numpy as np
import matplotlib.pyplot as plt


# Определение функции
def f(x):
    return -12 * (x ** 4) * np.sin(np.cos(x)) - 18 * (x ** 3) + 5 * (x ** 2) + 10 * x - 30


# Метод бисекции для поиска корней
def bisect(a, b, tol):
    c = (a + b) / 2.0
    while (b - a) / 2.0 > tol:
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
    return c


# Поиск корней
root1 = bisect(0, 0.5, 0.0001)
root2 = bisect(1, 1.5, 0.0001)
root3 = bisect(2.5, 3, 0.0001)

print("Корни функции:")
print(root1, root2, root3)


# Нахождение интервалов, на которых функция возрастает
def increasing_intervals(a, b, step=0.001):
    intervals = []
    while a < b:
        if f(a + step) > f(a):
            start = a
            while f(a + step) > f(a):
                a += step
            end = a
            intervals.append((start, end))
        a += step
    return intervals


print("\nИнтервалы, на которых функция возрастает:")
print(increasing_intervals(-5, 5))


# Нахождение интервалов, на которых функция убывает
def decreasing_intervals(a, b, step=0.001):
    intervals = []
    while a < b:
        if f(a + step) < f(a):
            start = a
            while f(a + step) < f(a):
                a += step
            end = a
            intervals.append((start, end))
        a += step
    return intervals


print("\nИнтервалы, на которых функция убывает:")
print(decreasing_intervals(-5, 5))

# Построение графика функции
x = np.linspace(-5, 5, 1000)
y = f(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid(True)
plt.show()

# Нахождение координат вершины функции
from scipy.optimize import minimize

x0 = 0
result = minimize(f, x0)
vertex = result.x, f(result.x)
print("\nКоординаты вершины функции:", vertex)


# Нахождение промежутков, на которых функция > 0
def positive_intervals(a, b, step=0.001):
    intervals = []
    while a < b:
        if f(a + step) > 0 and f(a) <= 0:
            start = a
            while f(a + step) > 0:
                a += step
            end = a
            intervals.append((start, end))
        a += step
    return intervals


print("\nПромежутки, на которых функция > 0:")
print(positive_intervals(-5, 5))


# Нахождение промежутков, на которых функция < 0
def negative_intervals(a, b, step=0.001):
    intervals = []
    while a < b:
        if f(a + step) < 0 and f(a) >= 0:
            start = a
            while f(a + step) < 0:
                a += step
            end = a
            intervals.append((start, end))
        a += step
    return intervals


print("\nПромежутки, на которых функция < 0:")
print(negative_intervals(-5, 5))
