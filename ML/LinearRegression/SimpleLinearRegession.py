import numpy as np


class SimpleLinearRegression1:
    def __init__(self):
        """初始化模型"""
        self.a_ = None
        self.b_ = None
        # 下划线代表不是用户传进来的

    def fit(self, x_train, y_train):
        """根据数据训练"""
        assert x_train.ndim == 1
        assert len(x_train) == len(y_train)

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        numerator = 0.0
        denominator = 0.0

        for x_i, y_i in zip(x_train, y_train):
            numerator += (x_i - x_mean) * (y_i - y_mean)
            denominator += (x_i - x_mean) ** 2

        self.a_ = numerator / denominator
        self.b_ = y_mean - self.a_ * x_mean

    def predict(self, x_predict):
        """给定预测数据集x_predict"""
        assert  x_predict.ndim == 1
        assert  self.a_ is not None and self.b_ is not None

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        """给定单个预测数据x_single，返回x的预测值"""

        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression1()"
