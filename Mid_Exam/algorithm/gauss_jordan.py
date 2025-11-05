import matplotlib.pyplot as plt

arr = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]
N = 3

def gauss_jordan(arr, N):
    solutions_steps = []
    
    for i in range(N):
        for j in range(N):
            if i != j:
                p = arr[j][i] / arr[i][i]
                for k in range(N+1):
                    arr[j][k] -= arr[i][k] * p
        current_solutions = [arr[x][N] / arr[x][x] for x in range(N)]
        solutions_steps.append(current_solutions.copy())
        
        print(f"After step {i+1}:")
        for row in arr:
            print(row)
        print()
    
    solutions = [arr[i][N] / arr[i][i] for i in range(N)]
    print("Final Solutions:", solutions)
    
    return solutions, solutions_steps

if __name__ == "__main__":
    solution, steps = gauss_jordan([row[:] for row in arr], N)

    variables = ['x', 'y', 'z']
    for i, step in enumerate(steps):
        plt.bar([v + f" (step {i+1})" for v in variables], step, alpha=0.7, label=f'Step {i+1}')

    plt.ylabel("Value")
    plt.title("Gauss-Jordan Elimination Steps")
    plt.grid(axis='y')
    plt.legend()
    plt.show()
