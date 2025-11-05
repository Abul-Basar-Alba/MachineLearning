import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1, 2, 1.3, 3.75, 2.25, 5.5])

degree = 2

coeffs = np.polyfit(x, y, degree)
poly_eq = np.poly1d(coeffs)

x_new = np.linspace(min(x), max(x), 100)
y_new = poly_eq(x_new)

print("Polynomial Coefficients:", coeffs)
print("Equation:", poly_eq)

plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_new, y_new, color='blue', label=f'Polynomial (degree {degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Regression')
plt.legend()
plt.grid(True)
plt.show()
