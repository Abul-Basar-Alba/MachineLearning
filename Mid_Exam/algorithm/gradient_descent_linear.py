import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=10000):
    n = len(y)
    for _ in range(epochs):
        y_pred = m * x + b
        dm = (-2/n) * sum(x * (y - y_pred))
        db = (-2/n) * sum(y - y_pred)
        m -= learning_rate * dm
        b -= learning_rate * db
    return m, b

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4], dtype=float)
    y = np.array([2, 3, 4, 5], dtype=float)

    m, b = gradient_descent(x, y, learning_rate=0.01, epochs=10000)

    print(f"Estimated slope (m) = {m:.4f}")
    print(f"Estimated intercept (b) = {b:.4f}")

    x_new = 5
    y_new = m * x_new + b
    print(f"Prediction for x={x_new}: y={y_new:.4f}")

    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x, m*x + b, color='blue', label=f'Fitted Line: y={m:.2f}x+{b:.2f}')
    plt.scatter(x_new, y_new, color='green', marker='*', s=100, label=f'Prediction at x={x_new}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Regression using Gradient Descent')
    plt.legend()
    plt.grid(True)
    plt.show()
