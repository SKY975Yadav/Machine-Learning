from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_excel("game.xlsx")

# print(df)

features = ["Kills","Assists","Damage"]
X = df[features]
y = df["Rank_Increase"]

# print(X)
# print(y)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(y_pred)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


# my own test


print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

data = np.array([8, 3, 3800]).reshape(1, -1)
tem = model.predict(data)
print(tem)