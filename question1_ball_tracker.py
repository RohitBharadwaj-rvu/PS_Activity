import numpy as np
import matplotlib.pyplot as plt

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
    X_T_X = np.dot(X_T, X_matrix)
    X_T_X_inv = np.linalg.inv(X_T_X)
    X_T_Y = np.dot(X_T, Y_matrix)
    
    beta = np.dot(X_T_X_inv, X_T_Y)
    
    c = beta[0]
    b = beta[1]
    a = beta[2]
    
    print(f"Parabolic Equation: y = {a:.5f}x^2 + {b:.5f}x + {c:.5f}")
    
    initial_height = c
    print(f"\na) The height from which the ball left the player's hand: {initial_height:.5f} metres")
    
    discriminant = (b**2) - (4 * a * c)
    root1 = (-b + np.sqrt(discriminant)) / (2 * a)
    root2 = (-b - np.sqrt(discriminant)) / (2 * a)
    
    range_estimate = root1 if root1 > 0 else root2
    print(f"b) Estimated range of the ball: {range_estimate:.5f} metres")

    x_curve = np.linspace(min(x_data), range_estimate, 500)
    y_curve = a * x_curve**2 + b * x_curve + c

    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='red', label='Noisy Sensor Data')
    plt.plot(x_curve, y_curve, color='blue', label='Fitted Parabolic Trajectory')
    plt.title('Ball Tracking Regression Model')
    plt.xlabel('Horizontal Distance (metres)')
    plt.ylabel('Height (metres)')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
