import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_gradient_descent(x, y, m=0, b=0, learning_rate=0.1, epochs=1000):
    n = len(y)
    for _ in range(epochs):
        z = m*x + b
        y_pred = sigmoid(z)
        dm = (1/n) * sum((y_pred - y) * x)
        db = (1/n) * sum(y_pred - y)
        m -= learning_rate * dm
        b -= learning_rate * db
    return m, b

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4], dtype=float)
    y = np.array([0, 0, 1, 1], dtype=float)

    m, b = logistic_gradient_descent(x, y, learning_rate=0.1, epochs=1000)

    print(f"Estimated slope (m) = {m:.4f}")
    print(f"Estimated intercept (b) = {b:.4f}")

    x_new = 5
    prob = sigmoid(m*x_new + b)
    pred_class = 1 if prob >= 0.5 else 0

    print(f"Prediction for x={x_new}: P(Y=1) = {prob:.4f}")
    print(f"Predicted class for x={x_new}: {pred_class}")

    x_curve = np.linspace(min(x)-1, max(x)+1, 200)
    y_curve = sigmoid(m*x_curve + b)

    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_curve, y_curve, color='blue', label='Logistic Regression Curve')
    plt.scatter(x_new, prob, color='green', marker='*', s=100, label=f'Prediction at x={x_new}')
    plt.axhline(0.5, color='gray', linestyle='--', linewidth=1, label='Decision Boundary')

    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Logistic Regression using Gradient Descent')
    plt.legend()
    plt.grid(True)
    plt.show()
