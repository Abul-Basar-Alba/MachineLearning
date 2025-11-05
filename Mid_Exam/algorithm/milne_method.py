import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def milne_method(x_values, y_values, h, x_to_find):
    predicted_points = []
    corrected_points = []

    while x_values[-1] < x_to_find:
        y_pred = y_values[-4] + (4 * h / 3) * (2*f(x_values[-3], y_values[-3]) 
                                               - f(x_values[-2], y_values[-2]) 
                                               + 2*f(x_values[-1], y_values[-1]))
        x_next = x_values[-1] + h
        predicted_points.append((x_next, y_pred))

        y_corr = y_values[-2] + (h / 3) * (f(x_values[-2], y_values[-2]) 
                                           + 4*f(x_values[-1], y_values[-1]) 
                                           + f(x_next, y_pred))
        corrected_points.append((x_next, y_corr))

        x_values.append(x_next)
        y_values.append(y_corr)

        print(f"x = {x_next:.4f}, Predicted y = {y_pred:.6f}, Corrected y = {y_corr:.6f}")

    return x_values, y_values, predicted_points, corrected_points

if __name__ == "__main__":
    x_values = [0, 0.1, 0.2, 0.3]
    y_values = [1, 1.1052, 1.2214, 1.3499]
    h = 0.1
    x_to_find = 0.4

    x_vals, y_vals, preds, corrs = milne_method(x_values, y_values, h, x_to_find)

    plt.plot(x_vals, y_vals, 'b-o', label='Corrected Solution', markersize=6)

    x_pred, y_pred = zip(*preds)
    plt.scatter(x_pred, y_pred, color='red', marker='x', s=80, label='Predicted Points')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Milne's Predictor-Corrector Method")
    plt.legend()
    plt.grid(True)
    plt.show()
