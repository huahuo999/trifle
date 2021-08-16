from LinearRegression.SimpleLinearRegession import SimpleLinearRegression1
import numpy as np

x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])

reg1 = SimpleLinearRegression1()
reg1.fit(x, y)

x_TestPredict = 6
reg1.predict(np.array(x_TestPredict))
reg1.predict()
