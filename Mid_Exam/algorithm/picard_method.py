import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def picard_method(x0, y0, x_end, n_iter=4, steps=100):
    h = (x_end - x0) / steps
    x_points = np.linspace(x0, x_end, steps + 1)
    
    approximations = []

    y_points = np.full_like(x_points, y0, dtype=float)
    
    for k in range(n_iter):
        y_new = np.zeros_like(y_points)
        y_new[0] = y0
        for i in range(1, len(x_points)):
            xi_1 = x_points[i-1]
            yi_1 = y_points[i-1]
            y_new[i] = yi_1 + h * f(xi_1, yi_1)
        y_points = y_new.copy()
        approximations.append(y_points)
        print(f"Iteration {k+1}: y({x_end}) ≈ {y_points[-1]:.6f}")

    return x_points, approximations

if __name__ == "__main__":
    x0 = 0
    y0 = 1
    x_end = 0.4
    n_iter = 4
    steps = 50

    x_points, approx_list = picard_method(x0, y0, x_end, n_iter, steps)

    plt.figure(figsize=(8,5))

    colors = ['red', 'green', 'blue', 'purple']
    for i, y_vals in enumerate(approx_list):
        plt.plot(x_points, y_vals, color=colors[i], label=f'Iteration {i+1}')

    y_exact = -x_points - 1 + 2*np.exp(x_points)
    plt.plot(x_points, y_exact, 'k--', label='Exact Solution')

    plt.scatter([x_end], [approx_list[-1][-1]], color='black', s=50, label=f'Approx y({x_end}) ≈ {approx_list[-1][-1]:.6f}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Picard's Iteration Method")
    plt.legend()
    plt.grid(True)
    plt.show()
