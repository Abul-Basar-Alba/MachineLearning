import numpy as np
import matplotlib.pyplot as plt

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A.astype(float), b.reshape(-1,1).astype(float)])
    steps = []
    
    print("Initial Augmented Matrix [A|b]:")
    print(Ab)
    print()
    
    for i in range(n):
        pivot = Ab[i][i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered!")
        Ab[i] = Ab[i] / pivot
        
        for j in range(i+1, n):
            factor = Ab[j][i]
            Ab[j] = Ab[j] - factor * Ab[i]
        
        x_est = np.zeros(n)
        for k in range(i+1):
            x_est[k] = Ab[k, -1]
        steps.append(x_est.copy())
        
        print(f"After eliminating column {i+1}:")
        print(Ab)
        print()
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = Ab[i,-1] - np.sum(Ab[i, i+1:n]*x[i+1:n])
    
    return x, steps

if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)

    solution, steps = gauss_elimination(A, b)
    print("Solution vector x =", solution)

    variables = ['x', 'y', 'z']
    for i, step in enumerate(steps):
        plt.bar([v + f" (step {i+1})" for v in variables], step, alpha=0.7, label=f'Step {i+1}')

    plt.ylabel("Value")
    plt.title("Gauss Elimination: Forward Elimination Steps")
    plt.grid(axis='y')
    plt.legend()
    plt.show()
