import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([1, 2, 3, 4]).reshape(-1, 1)
Y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, Y)

m = model.coef_[0][0]
c = model.intercept_[0]

print(f"Equation: P(Y=1) = 1 / (1 + exp(-({m:.4f}*X + {c:.4f})))")

X_new = np.array([[5]])
prob = model.predict_proba(X_new)[0][1]
print(f"Prediction for X={X_new[0][0]}: P(Y=1) = {prob:.4f}")

pred_class = model.predict(X_new)[0]
print(f"Predicted class for X={X_new[0][0]}: {pred_class}")

X_curve = np.linspace(0, 6, 200).reshape(-1, 1)
Y_curve = model.predict_proba(X_curve)[:, 1]

plt.scatter(X, Y, color='red', label='Data Points')
plt.plot(X_curve, Y_curve, color='blue', label='Logistic Regression Curve')
plt.scatter(X_new, prob, color='green', marker='*', s=150, label=f'Prediction at X={X_new[0][0]}')
plt.axhline(0.5, color='gray', linestyle='--', linewidth=1, label='Decision Boundary')

plt.xlabel('X')
plt.ylabel('Probability of Y=1')
plt.title('Logistic Regression using scikit-learn')
plt.legend()
plt.grid(True)
plt.show()
