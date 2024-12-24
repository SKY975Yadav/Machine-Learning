import numpy as np
from sklearn.model_selection import LeavePOut
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Leave-P-Out Cross-Validation with p=2
lpo = LeavePOut(p=2)
model = LogisticRegression(max_iter=200)

accuracies = []

# Perform Leave-P-Out Cross-Validation
for train_index, test_index in lpo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))

# Calculate average accuracy
average_accuracy = np.mean(accuracies)
print(f"Average Accuracy: {average_accuracy:.2f}")
