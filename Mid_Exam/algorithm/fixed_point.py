import math
import matplotlib.pyplot as plt

def g(x):
    return (x**3 + 1) / 4

def fixed_point(x0, tol, n):
    print("Iteration\t x")
    i = 1
    x_values = [x0]
    
    while n > 0:
        x1 = g(x0)
        x_values.append(x1)
        print(f"{i}\t\t {x1:.6f}")
        i += 1
        
        if abs(x1 - x0) < tol:
            print("\nConverged!")
            break
        x0 = x1
        n -= 1
    
    print("\nApproximate root:", x1)
    return x1, x_values

if __name__ == "__main__":
    x0 = 0.5
    tol = 1e-5
    n = 100

    ans, x_values = fixed_point(x0, tol, n)

    plt.figure(figsize=(8,5))
    plt.plot(range(len(x_values)), x_values, 'bo-', markersize=5)
    plt.axhline(y=ans, color='r', linestyle='--', label=f'Converged root ≈ {ans:.6f}')
    plt.xlabel('Iteration')
    plt.ylabel('x (estimate)')
    plt.title('Fixed-Point Iteration Convergence')
    plt.grid(True)
    plt.legend()
    plt.show()
