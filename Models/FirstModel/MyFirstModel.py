import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# USING BUILT IN DATASET : 

# from sklearn.datasets import load_diabetes

# diabetes = load_diabetes()
# X = diabetes.data
# y = diabetes.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f'Mean Squared Error: {mse}')
# print(f'R-squared: {r2}')

# print(f'Coefficients: {model.coef_}')
# print(f'Intercept: {model.intercept_}')


# USING EXTERNAL DATA SET :

# Read data from data set

df = pd.read_excel("mobile_data.xlsx")


from sklearn.preprocessing import LabelEncoder

# Encode categorical variable
label_encoder = LabelEncoder()
df['Mobile Name'] = label_encoder.fit_transform(df['Mobile Name'])

# Check for missing values
print(df.isnull().sum())

# Fill missing values with mean (if applicable)
df.fillna(df.mean(), inplace=True)

from sklearn.preprocessing import StandardScaler

# Standardize numerical features
features = ['Camera Quality (MP)','Processor Speed (GHz)', 'RAM (GB)', 'Storage (GB)', 'Build Cost ($)', 'Display Refresh Rate (Hz)', 'Battery Capacity (mAh)']
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Example: Drop the 'Mobile Name' column if not needed
df = df.drop(columns=['Mobile Name'])


X = df[features]
y = df['Price ($)']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train)
print(X_test)
print(y_train)
print(y_test)


model = LinearRegression()
model.fit(X_train,y_train)


# Testing
y_pred = model.predict(X_test)

print(X_test)
print(y_pred)
# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')




# This is interesting if i remove ram and storage it gives the more accurate predection

# Read data from data set

# df = pd.read_excel("updated_mob_data.xlsx")


# from sklearn.preprocessing import LabelEncoder

# # Encode categorical variable
# label_encoder = LabelEncoder()
# df['Mobile Name'] = label_encoder.fit_transform(df['Mobile Name'])

# # Check for missing values
# print(df.isnull().sum())

# # Fill missing values with mean (if applicable)
# df.fillna(df.mean(), inplace=True)

# from sklearn.preprocessing import StandardScaler

# # Standardize numerical features
# features = ['Camera Quality (MP)','Processor Speed (GHz)', 'Build Cost ($)', 'Display Refresh Rate (Hz)', 'Battery Capacity (mAh)']
# scaler = StandardScaler()
# df[features] = scaler.fit_transform(df[features])

# # Example: Drop the 'Mobile Name' column if not needed
# df = df.drop(columns=['Mobile Name'])


# X = df[features]
# y = df['Price ($)']

# # Splitting the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)


# model = LinearRegression()
# model.fit(X_train,y_train)


# # Testing
# y_pred = model.predict(X_test)

# print(X_test)
# print(y_pred)
# # Evaluating the model
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f'Mean Squared Error: {mse}')
# print(f'R-squared: {r2}')

