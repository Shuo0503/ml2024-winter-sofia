import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))
    
    ground_truth = []
    predicted = []
    
    for i in range(N):
        x = int(input(f"Enter ground truth class label for point {i + 1} (0 or 1): "))
        y = int(input(f"Enter predicted class label for point {i + 1} (0 or 1): "))
        ground_truth.append(x)
        predicted.append(y)
    
    precision = precision_score(ground_truth, predicted)
    recall = recall_score(ground_truth, predicted)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
