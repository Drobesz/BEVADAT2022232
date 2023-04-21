import numpy as np
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3) -> None:
        self.epochs = epochs
        self.lr = lr
        self.m, self.c = 0

    def fit(self, X: np.array, y: np.array):
        n = float(len(X))
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m * X + self.c  # The current predicted value of Y
            residuals = y_pred - y
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2 / n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2 / n) * sum(residuals)  # Derivative wrt c
            self.m = self.m - self.lr * - D_m  # Update m
            self.c = self.c - self.lr * - D_c  # Update c
        return losses

    def predict(self, X):
        pred = []
        for x in X:
            pred.append(self.m * x + self.c)
        return np.array(pred)
