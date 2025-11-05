import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1, 2],
    [2, 3],
    [4, 5],
    [3, 6]
], dtype=float)

y = np.array([3, 5, 9, 8], dtype=float)

X_b = np.c_[np.ones((X.shape[0], 1)), X]

B = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
print("Coefficients (b0, b1, b2):", B)

y_pred = X_b @ B

plt.scatter(y, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Perfect Fit')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Multiple Regression: Predicted vs Actual')
plt.legend()
plt.grid(True)
plt.show()
