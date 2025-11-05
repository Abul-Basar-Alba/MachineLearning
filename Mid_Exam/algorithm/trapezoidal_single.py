import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + x**2)

a = 0
b = 1

integral = (b - a) * (f(a) + f(b)) / 2
print(f"Integral using single-interval Trapezoidal Rule: {integral:.6f}")

x = np.linspace(a-0.1, b+0.1, 200)
y = f(x)

plt.plot(x, y, color='blue', label='f(x) = 1/(1+x^2)')
plt.fill_between(x, y, where=(x >= a) & (x <= b), color='orange', alpha=0.3, label='Trapezoid Area')

plt.plot([a, b], [f(a), f(a)], color='orange')
plt.plot([a, b], [f(b), f(b)], color='orange')
plt.plot([a, a], [0, f(a)], color='orange')
plt.plot([b, b], [0, f(b)], color='orange')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Single-Interval Trapezoidal Rule')
plt.legend()
plt.grid(True)
plt.show()
