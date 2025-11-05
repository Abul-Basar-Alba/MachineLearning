import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return 200.0 * np.log(140000.0 / (140000.0 - 2100.0 * x)) - 9.8 * x

def simpson_three_eighth_single(a, b):
    h = (b - a) / 3
    x0 = a
    x1 = a + h
    x2 = a + 2*h
    x3 = b
    return (b - a) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3)) / 8

def trapezoidal_basic(a, b):
    return (b - a) * (f(a) + f(b)) / 2

if __name__ == "__main__":
    a = 0
    b = 1

    simpson_3_8_result = simpson_three_eighth_single(a, b)
    trapezoid_result = trapezoidal_basic(a, b)

    print(f"Simpson's 3/8 Rule (single interval): {simpson_3_8_result:.6f}")
    print(f"Basic Trapezoidal Rule (single interval): {trapezoid_result:.6f}")

    x = np.linspace(a-0.1, b+0.1, 200)
    y = f(x)

    plt.plot(x, y, color='blue', label='f(x)')

    plt.fill_between(x, y, where=(x >= a) & (x <= b), color='orange', alpha=0.3, label='Trapezoid Area')

    x0, x1, x2, x3 = a, a + (b-a)/3, a + 2*(b-a)/3, b
    x_cubic = np.linspace(a, b, 100)
    y_cubic = (
        f(x0) * (x_cubic-x1)*(x_cubic-x2)*(x_cubic-x3)/((x0-x1)*(x0-x2)*(x0-x3)) +
        f(x1) * (x_cubic-x0)*(x_cubic-x2)*(x_cubic-x3)/((x1-x0)*(x1-x2)*(x1-x3)) +
        f(x2) * (x_cubic-x0)*(x_cubic-x1)*(x_cubic-x3)/((x2-x0)*(x2-x1)*(x2-x3)) +
        f(x3) * (x_cubic-x0)*(x_cubic-x1)*(x_cubic-x2)/((x3-x0)*(x3-x1)*(x3-x2))
    )
    plt.fill_between(x_cubic, y_cubic, color='green', alpha=0.3, label="Simpson's 3/8 Area")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("Trapezoidal vs Simpson's 3/8 Rule")
    plt.legend()
    plt.grid(True)
    plt.show()
