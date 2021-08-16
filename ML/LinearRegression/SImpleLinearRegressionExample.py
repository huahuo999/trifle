import numpy as np
import matplotlib.pyplot as plt

x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])

plt.scatter(x, y)
plt.axis([0, 6, 0, 6])
plt.show()

x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = 0.0
denominator = 0.0

for x_i, y_i in zip(x, y):
    numerator += (x_i - x_mean) * (y_i - y_mean)
    denominator += (x_i - x_mean) ** 2

a = numerator / denominator
b = y_mean - a * x_mean


y_predict = a*x+b
plt.scatter(x, y)
plt.plot(x, y_predict, color='r')
plt.axis([0, 6, 0, 6])
plt.show()

x_TestPredict = 6
y_TestPredict = a*x_TestPredict+b
print("预测y值为", y_TestPredict)
