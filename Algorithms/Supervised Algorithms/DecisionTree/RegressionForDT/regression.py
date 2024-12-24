import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Create a simple dataset
# X: Feature (1D array), y: Target values (squared function with some noise)
X = np.arange(1, 11).reshape(-1, 1)
y = np.array([1.5, 2.7, 5.0, 6.1, 7.5, 9.1, 12.0, 15.0, 18.3, 20.5])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Regressor model
regressor = DecisionTreeRegressor(random_state=42)

# Train the model using the training data
regressor.fit(X_train, y_train)
# Predict using the trained model
y_pred = regressor.predict(X_test)

# Print predictions and true values
print("Predicted values:", y_pred)
print("True values:", y_test)
# For smooth curve, create a finer grid of X values
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)

# Predict values for the finer grid
y_grid_pred = regressor.predict(X_grid)

# Plot the original data points
plt.scatter(X, y, color='red', label="Original Data")

# Plot the decision tree regression curve
plt.plot(X_grid, y_grid_pred, color='blue', label="Regression Line")

# Add labels and title
plt.title('Decision Tree Regression')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()
