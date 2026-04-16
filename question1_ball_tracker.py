import numpy as np
import matplotlib.pyplot as plt

def gaussian_elimination(A, b):
    n = len(b)
    augmented = np.zeros((n, n + 1))
    for i in range(n):
        for j in range(n):
            augmented[i][j] = A[i][j]
        augmented[i][n] = b[i]

    for col in range(n):
        max_row = col
        for row in range(col + 1, n):
            if abs(augmented[row][col]) > abs(augmented[max_row][col]):
                max_row = row
        temp = augmented[col].copy()
        augmented[col] = augmented[max_row]
        augmented[max_row] = temp

        for row in range(col + 1, n):
            factor = augmented[row][col] / augmented[col][col]
            for j in range(col, n + 1):
                augmented[row][j] = augmented[row][j] - factor * augmented[col][j]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - augmented[i][j] * x[j]
        x[i] = x[i] / augmented[i][i]

    return x

def main():
    x_data = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
    y_data = [1.60000, 2.72566, 3.79325, 4.80277, 5.75421, 6.64758, 7.48287, 8.26009, 8.97923,
              9.64030, 10.24330, 10.78822, 11.27507, 11.70385, 12.07455, 12.38717, 12.64173,
              12.83821, 12.97661, 13.05694, 13.07920, 13.04338, 12.94949, 12.79752, 12.58748]

    X = []
    for x in x_data:
        X.append([1, x, x**2])

    X_matrix = np.array(X)
    Y_matrix = np.array(y_data)

    X_T = X_matrix.transpose()
    A = np.dot(X_T, X_matrix)
    b = np.dot(X_T, Y_matrix)

    print("Normal Equation System: A * beta = b")
    print(f"A (X^T X) =\n{A}")
    print(f"b (X^T Y) = {b}")

    beta = gaussian_elimination(A, b)

    c = beta[0]
    b_coeff = beta[1]
    a = beta[2]

    print(f"\nSolved using Gaussian Elimination:")
    print(f"Parabolic Equation: y = {a:.5f}x^2 + {b_coeff:.5f}x + {c:.5f}")

    initial_height = c
    print(f"\na) The height from which the ball left the player's hand: {initial_height:.5f} metres")

    discriminant = (b_coeff**2) - (4 * a * c)
    root1 = (-b_coeff + np.sqrt(discriminant)) / (2 * a)
    root2 = (-b_coeff - np.sqrt(discriminant)) / (2 * a)

    range_estimate = root1 if root1 > 0 else root2
    print(f"b) Estimated range of the ball: {range_estimate:.5f} metres")

    x_curve = np.linspace(min(x_data), range_estimate, 500)
    y_curve = a * x_curve**2 + b_coeff * x_curve + c

    y_pred = [a * x**2 + b_coeff * x + c for x in x_data]
    residuals = [y_data[i] - y_pred[i] for i in range(len(x_data))]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [2, 1]})
    
    # Top Subplot: Trajectory
    ax1.scatter(x_data, y_data, color='red', label='Sensor Data')
    ax1.plot(x_curve, y_curve, color='blue', label='Fitted Parabolic Trajectory')
    ax1.set_title('Ball Tracking - Quadratic Regression (Gaussian Elimination)')
    ax1.set_ylabel('Height (metres)')
    ax1.axhline(0, color='black', linewidth=1)
    ax1.axvline(0, color='black', linewidth=1)
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.7)

    # Bottom Subplot: Residuals
    ax2.scatter(x_data, residuals, color='purple', label='Residual Error')
    ax2.axhline(0, color='black', linewidth=1, linestyle='--')
    ax2.set_title('Residual Analysis (y_actual - y_predicted)')
    ax2.set_xlabel('Horizontal Distance (metres)')
    ax2.set_ylabel('Residual Error (metres)')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('q1_output.png', dpi=150, bbox_inches='tight')
    # plt.show() # Disabled inside automated scripts for faster runs

if __name__ == "__main__":
    main()
