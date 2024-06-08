import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

class NumberProcessor:
    def __init__(self):
        self.N = 0
        self.points = []

    def read_N(self):
        self.N = int(input("Enter the number of points (N): "))

    def read_points(self):
        for i in range(self.N):
            x = float(input(f"Enter x-coordinate for point {i + 1}: "))
            y = float(input(f"Enter y-coordinate for point {i + 1}: "))
            self.points.append((x, y))

    def k_nn_regression(self, k, X):
        if k <= self.N:
            x_values = np.array([point[0] for point in self.points])
            y_values = np.array([point[1] for point in self.points])
            
            x_values = x_values.reshape(-1, 1)  # Reshape for sklearn
            model = KNeighborsRegressor(n_neighbors=k)
            model.fit(x_values, y_values)
            
            predicted_y = model.predict(np.array([[X]]))
            coefficient_of_determination = r2_score(y_values, model.predict(x_values))
            
            return predicted_y[0], coefficient_of_determination
        else:
            return "Error: k should be less than or equal to N"

def main():
    processor = NumberProcessor()
    processor.read_N()
    processor.read_points()

    k = int(input("Enter the value of k: "))
    X = float(input("Enter the value of X: "))

    result, r2 = processor.k_nn_regression(k, X)
    if isinstance(result, float):
        print(f"Result (Y): {result}")
        print(f"Coefficient of Determination (R^2): {r2}")
    else:
        print(result)

if __name__ == "__main__":
    main()