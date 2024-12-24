from sklearn.linear_model import LinearRegression

# Example dataset
X = [[2000, 3, 5], [1500, 2, 10], [1800, 4, 3]]  # [Size, Bedrooms, Distance from City]
y = [250000, 180000, 220000]  # House prices

# Create model
model = LinearRegression()
model.fit(X, y)

# Get coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

