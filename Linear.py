#Simple Linear Regression
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X, y)

pred_y = regressor.predict(X)

plt.plot(x, pred_y)
plt.plot(x, y)