import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson_plot(x0, tol=1e-6, max_iter=100):
    x_values = [x0]
    print("Iteration\t x")
    for i in range(max_iter):
        x1 = x0 - f(x0)/df(x0)
        x_values.append(x1)
        print(f"{i+1}\t\t {x1:.6f}")
        
        if abs(x1 - x0) < tol:
            print("\nRoot found at:", round(x1, 6))
            break
        x0 = x1
    else:
        print("Did not converge.")
    
    plt.plot(range(len(x_values)), x_values, marker='o', color='blue')
    plt.xlabel('Iteration')
    plt.ylabel('x value')
    plt.title('Newton-Raphson Convergence')
    plt.grid(True)
    plt.show()

    return x_values[-1]

if __name__ == "__main__":
    x0 = 1.5
    newton_raphson_plot(x0)
