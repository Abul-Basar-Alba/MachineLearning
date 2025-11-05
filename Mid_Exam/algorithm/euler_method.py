import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def euler_method(x0, y0, x_end, h):
    n = int((x_end - x0) / h)
    x_points = [x0]
    y_points = [y0]

    x = x0
    y = y0

    print("x\t\ty")
    print(f"{x0:.4f}\t{y0:.6f}")

    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_points.append(x)
        y_points.append(y)
        print(f"{x:.4f}\t{y:.6f}")

    return np.array(x_points), np.array(y_points)

if __name__ == "__main__":
    x0 = 0
    y0 = 1
    x_end = 0.4
    h = 0.1

    x_points, y_points = euler_method(x0, y0, x_end, h)

    x_exact = np.linspace(x0, x_end, 100)
    y_exact = -x_exact - 1 + 2*np.exp(x_exact)

    plt.figure(figsize=(8,5))
    plt.plot(x_points, y_points, 'bo-', label="Euler's Method", markersize=6)
    plt.plot(x_exact, y_exact, 'r--', label='Exact Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Euler's Method Approximation")
    plt.legend()
    plt.grid(True)
    plt.show()
