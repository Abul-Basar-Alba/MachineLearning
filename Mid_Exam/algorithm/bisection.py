import math
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x + 1

def bisection(a, b, tol, n):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None, []

    print("Iteration\t a\t\t b\t\t c\t\t f(c)")
    i = 1
    c_values = []
    
    while i <= n:
        c = (a + b) / 2
        c_values.append(c)
        print(f"{i}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")
        i += 1
        
        if abs(f(c)) < tol or abs(b - a)/2 < tol:
            print("\nConverged!")
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    print("\nApproximate root:", c)
    return c, c_values

if __name__ == "__main__":
    a = 0
    b = 1
    tol = 1e-5
    n = 200

    root, c_values = bisection(a, b, tol, n)

    plt.figure(figsize=(8,5))
    plt.plot(range(1, len(c_values)+1), c_values, 'bo-', markersize=5)
    plt.axhline(y=root, color='r', linestyle='--', label=f'Converged root ≈ {root:.6f}')
    plt.xlabel('Iteration')
    plt.ylabel('c (midpoint estimate)')
    plt.title('Bisection Method Convergence')
    plt.grid(True)
    plt.legend()
    plt.show()
