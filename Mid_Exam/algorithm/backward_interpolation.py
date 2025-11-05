import matplotlib.pyplot as plt

def backward_interpolation(x_values, y_values, x):
    n = len(x_values)
    diff_table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        diff_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

    print("Backward Difference Table:")
    for i in range(n):
        print(diff_table[i][:i + 1])

    h = x_values[1] - x_values[0]
    p = (x - x_values[-1]) / h
    result = y_values[-1]

    for i in range(1, n):
        p_term = p
        for j in range(1, i):
            p_term *= (p + j)
        result += (p_term * diff_table[-1][i]) / factorial(i)

    return result

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    x_values = [0, 1, 2, 3, 4]
    y_values = [1, 8, 27, 64, 125]
    x = 2.5

    y_interp = backward_interpolation(x_values, y_values, x)
    print(f"\nInterpolated value at x = {x} is {y_interp:.6f}")

    plt.scatter(x_values, y_values, color='red', label='Data Points')
    plt.scatter(x, y_interp, color='green', marker='*', s=150, label=f'Interpolated Value at x={x}')

    x_smooth = [i*0.1 for i in range(0, 41)]
    y_smooth = [i**3 for i in x_smooth]
    plt.plot(x_smooth, y_smooth, color='blue', linestyle='--', label='Actual Function f(x)=x^3')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Backward Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()
