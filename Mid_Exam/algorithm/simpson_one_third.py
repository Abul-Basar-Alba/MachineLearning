import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 200.0 * np.log(140000.0 / (140000.0 - 2100.0 * x)) - 9.8 * x

def simpson_single_interval(a, b):
    x0 = a
    x2 = b
    x1 = (a + b) / 2
    return (b - a) * (f(x0) + 4*f(x1) + f(x2)) / 6

def trapezoidal_basic(a, b):
    return (b - a) * (f(a) + f(b)) / 2

if __name__ == "__main__":
    a = 0
    b = 1

    simpson_result = simpson_single_interval(a, b)
    trapezoid_result = trapezoidal_basic(a, b)

    print(f"Simpson's 1/3 Rule (single interval): {simpson_result:.6f}")

    x = np.linspace(a-0.1, b+0.1, 200)
    y = f(x)

    plt.plot(x, y, color='blue', label='f(x)')

    plt.fill_between(x, y, where=(x >= a) & (x <= b), color='orange', alpha=0.3, label='Trapezoid Area')

    x0, x1, x2 = a, (a+b)/2, b
    x_parabola = np.linspace(a, b, 100)
    y_parabola = f(x0) * (x_parabola - x1)*(x_parabola - x2)/((x0 - x1)*(x0 - x2)) + \
                 f(x1) * (x_parabola - x0)*(x_parabola - x2)/((x1 - x0)*(x1 - x2)) + \
                 f(x2) * (x_parabola - x0)*(x_parabola - x1)/((x2 - x0)*(x2 - x1))
    plt.fill_between(x_parabola, y_parabola, color='green', alpha=0.3, label="Simpson's 1/3 Area")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("Trapezoidal vs Simpson's 1/3 Rule")
    plt.legend()
    plt.grid(True)
    plt.show()
