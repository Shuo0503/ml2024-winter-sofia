import numpy as np

def knn_regression(Points, y_value, test_x, k):
    distances = np.sqrt(np.sum((Points - test_x)**2, axis=1))
    nearest_indices = np.argsort(distances)[:k]
    nearest_values = y_value[nearest_indices]
    return np.mean(nearest_values)

class FindNumber():
    def __init__(self, k, total_number):
        self.total_number = total_number
        self.k = k
        self.get_number(total_number)
        self.data_search(k, total_number)

    def get_number(self, total_number):
        self.Points = np.zeros((total_number, 2))
        self.y_value = np.zeros(total_number)
        for i in range(total_number):
            while True:
                try:
                    x = float(input("Please input the x value: "))
                    y = float(input("Please input the y value: "))
                    break
                except ValueError:
                    print("Please enter real numbers.")
            self.Points[i] = [x, y]
            self.y_value[i] = y
    
    
    def data_search(self, k, total_number):
        try:
            self.test_x = float(input("Please input the x use for prediction: "))
        except ValueError:
            print(("Please enter real numbers."))
        if k <= total_number:
            prediction = knn_regression(self.Points, self.y_value, np.array([[self.test_x, 0]]), k)
            print("The predicted value for " + str(self.test_x) + " is: " + str(prediction))
        else:
            print("k cannot be larger than the amount of points")
    
def main():
    while True:
        try:
            total_number = int(input("Please input the amount of points you will provide later: "))
            if total_number > 0:
                break
            else:
                print("Please input a positive integer.")
        except ValueError:
            print("Please input an integer")

    while True:
        try:
            k = int(input("Please input the k number you want to use for k-NN regression: "))
            if 0 < k <= total_number:
                break
            else:
                print("Please input a positive integer that is smaller than the numbers of points.")
        except ValueError:
            print("Please input an integer.")
    FindNumber(k, total_number)

main()
    