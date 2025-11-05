import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4], dtype=float)
Y = np.array([2, 3, 4, 5], dtype=float)
n = len(X)

m = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y)) / (n*np.sum(X**2) - (np.sum(X))**2)
c = (np.sum(Y) - m*np.sum(X)) / n

print(f"Equation: Y = {m:.2f}X + {c:.2f}")

X_new = 5
Y_new = m*X_new + c
print(f"Prediction for X={X_new}: {Y_new:.2f}")

plt.scatter(X, Y, color='red', label='Data Points')
plt.plot(X, m*X + c, color='blue', label=f'Fitted Line: Y={m:.2f}X+{c:.2f}')
plt.scatter(X_new, Y_new, color='green', marker='*', s=100, label=f'Prediction at X={X_new}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
