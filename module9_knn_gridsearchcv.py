import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Enter the number of training data points (N): "))
    train_data = []
    for i in range(N):
        x = float(input(f"Enter x-coordinate for training point {i + 1}: "))
        y = int(input(f"Enter class label for training point {i + 1} (non-negative integer): "))
        train_data.append((x, y))
    
    M = int(input("Enter the number of test data points (M): "))
    test_data = []
    for i in range(M):
        x = float(input(f"Enter x-coordinate for test point {i + 1}: "))
        y = int(input(f"Enter class label for test point {i + 1} (non-negative integer): "))
        test_data.append((x, y))
    
    best_k = -1
    best_accuracy = 0
    
    for k in range(1, 11):
        classifier = KNeighborsClassifier(n_neighbors=k)
        train_X = np.array([point[0] for point in train_data]).reshape(-1, 1)
        train_y = np.array([point[1] for point in train_data])
        test_X = np.array([point[0] for point in test_data]).reshape(-1, 1)
        test_y = np.array([point[1] for point in test_data])
        
        classifier.fit(train_X, train_y)
        predicted_y = classifier.predict(test_X)
        accuracy = accuracy_score(test_y, predicted_y)
        
        if accuracy > best_accuracy:
            best_k = k
            best_accuracy = accuracy
    
    print(f"Best k for k-NN Classifier: {best_k}")
    print(f"Corresponding Accuracy: {best_accuracy:.2f}")

if __name__ == "__main__":
    main()
