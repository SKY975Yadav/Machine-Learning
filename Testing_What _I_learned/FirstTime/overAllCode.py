import pandas as pd
import numpy as np
from sklearn import linear_model


df = pd.read_csv("AmesHousing.csv")
df


import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set(style="whitegrid")

# Histogram of SalePrice
plt.figure(figsize=(10, 6))
sns.histplot(df['SalePrice'], bins=30, kde=True)
plt.title('Distribution of Sale Price')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.show()

# Box Plot for SalePrice
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['SalePrice'])
plt.title('Box Plot of Sale Price')
plt.show()

# Scatter Plot: Gr Liv Area vs Sale Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Gr Liv Area', y='SalePrice', data=df)
plt.title('Scatter Plot: Gr Liv Area vs Sale Price')
plt.xlabel('Gr Liv Area')
plt.ylabel('Sale Price')
plt.show()


# Box plot to identify outliers in Sale Price
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['SalePrice'])
plt.title('Box Plot of Sale Price')
plt.show()

# Handling outliers: Removing outliers based on z-score
from scipy import stats

z_scores = np.abs(stats.zscore(df['SalePrice']))
df_no_outliers = df[(z_scores < 3)]  # Keep data within 3 standard deviations
df = df_no_outliers
df = df.reset_index()
df


# List of columns fill NaN values with their means
features = ['Garage Area', 'Wood Deck SF', 'Open Porch SF', 'Screen Porch', 'Lot Frontage', '1st Flr SF', 'Gr Liv Area']

# Fill NaN values in the specified columns with their column mean in one go
df[features] = df[features].fillna(df[features].mean())
df


# Removing the coloumns
df.dropna(axis=1,inplace = True,how='any')
df

# Encoding :

cols = df.select_dtypes(include='object').columns

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in cols:
    df[col] = le.fit_transform(df[col])

df

# dividing data into dependent and independent
X = df.drop("SalePrice",axis = 1)
y = df["SalePrice"]

# Standardization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Standardize the data and convert back to a DataFrame, keeping the original column names
df_standardized = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
df_standardized


# Splitting Data

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)



# Model Training
model = linear_model.LinearRegression()

model.fit(X_train,y_train)
print("Slope / coffeint " ,model.coef_[0])
print("Intercet ", model.intercept_)


# Predicting
y_pred = model.predict(X_test)

# Checking Accuracy
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test,y_pred)
print("MSE : ",mse)
r2 = r2_score(y_test,y_pred)
print("R2 _ Score : ",r2)


from sklearn.metrics import mean_absolute_error

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

# Visualizing Predicted vs Actual
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r', lw=2)
plt.xlabel('Actual Sale Price')
plt.ylabel('Predicted Sale Price')
plt.title('Actual vs Predicted Sale Price')
plt.show()



temp = df.loc[(23,24), : ]

temp = temp.drop(columns='SalePrice',axis = 1)

pred = model.predict(temp)
print(pred)