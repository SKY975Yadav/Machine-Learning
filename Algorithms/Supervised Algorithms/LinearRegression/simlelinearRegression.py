import numpy as np
from sklearn import linear_model

no_hours = np.array([5,6,3,4]).reshape(-1, 1)
marks = np.array([80,90,50,60])

model = linear_model.LinearRegression()

model.fit(no_hours,marks)

print("Slope / coffeint " ,model.coef_[0])
print("Intercet ", model.intercept_)

testCase = np.array([5,9]).reshape(-1,1)

testRes = model.predict(testCase)

print("Test Result : ", testRes)

