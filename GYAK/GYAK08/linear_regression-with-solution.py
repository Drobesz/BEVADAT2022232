import numpy as np


class LinearRegression:
    """
    Linear Regression Using Gradient Descent.
    Parameters
    ----------
    lr : float
        Learning rate
    n_iterations : int
        No of passes over the training set
    Attributes
    ----------
    weights : weights/ after fitting the model
    losses : total error of the model after each iteration
    """

    def __init__(self, lr=0.005, n_iterations=1000, early_stopping = 0.):
        self.lr = lr
        self.n_iterations = n_iterations
        self.early_stopping = early_stopping

    def fit(self, X, y):
        """
        Fit the training data
        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            Training samples
        y : array-like, shape = [n_samples, n_target_values]
            Target values
        """

        self.losses = []
        self.weights = np.zeros((X.shape[1], 1))

        """
        Run the gradient descent algorithm
        """
        for _ in range(self.n_iterations):
            """
            Calculate residuals
            """
            # Predict the output
            y_pred = np.dot(X, self.weights)

            # Calculate the residuals (residuals = y_pred - y)
            residuals = y_pred - y

            """
            Calculate gradient
            """
            gradient_vector = np.dot(X.T, residuals)

            # Update the weights
            self.weights -= self.lr * gradient_vector

            # Store loss (summ of residuals squared)
            loss = np.sum((residuals**2))
            self.losses.append(loss)
            if loss < self.early_stopping:
                print(f'Loss limit reached: {loss}')
                break
        print("Training done!")    

    def predict(self, X):
        """Predicts the value after the model has been trained.
        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            Test samples
        Returns
        -------
        Predicted value
        """

        return np.dot(X, self.weights)
