import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

if __name__ == "__main__":
    x_values = [0, 1, 2, 3, 4]
    y_values = [1, 8, 27, 64, 125]
    x = 2.5

    y_interp = lagrange_interpolation(x_values, y_values, x)
    print(f"Interpolated value at x = {x} is {y_interp:.6f}")

    plt.scatter(x_values, y_values, color='red', label='Data Points')
    plt.scatter(x, y_interp, color='green', marker='*', s=150, label=f'Interpolated Value at x={x}')

    x_smooth = [i*0.1 for i in range(0, 41)]
    y_smooth = [i**3 for i in x_smooth]
    plt.plot(x_smooth, y_smooth, color='blue', linestyle='--', label='Actual Function f(x)=x^3')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()
