import numpy as np
from sklearn.linear_model import LinearRegression
x_train = np.array([1, 2, 3, 4, 5, 8, 10]).reshape(-1, 1)
y_train = np.array([30, 35, 40, 48, 55, 75, 85])
model = LinearRegression()
model.fit(x_train, y_train)
prediction = model.predict([[70.5]])
print(f"Predicted Salary for 7.5 years: ${prediction[0]:.2f}k")
