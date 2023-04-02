import seaborn as sns
import numpy as np
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    
    @property
    def k_neighbors(self):
        return self.k
    
    def __init__(self, k : int, test_split_ratio : float):
        self.k = k
        self.test_split_ratio = test_split_ratio
    
    def train_test_split(self, features : pd.DataFrame, labels : pd.DataFrame) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features[:train_size, :], labels[:train_size]
        self.x_test, self.y_test = features[train_size : train_size + test_size, :], labels[train_size : train_size + test_size]
    
    def euclidean(self, element_of_x : pd.DataFrame) -> pd.DataFrame:
        return ((self.x_train - element_of_x)**2).sum(axis=1).pow(1./2)
    
    def predict(self, x_test:pd.DataFrame) -> None:
        labels_pred = []
        for x_test_element in x_test:
            distances = self.euclidean(x_test_element)
            distances = np.array(sorted(zip(distances, self.y_train)))
            label_pred = mode(distances[:self.k, 1], keepdims = False).mode
            labels_pred.append(label_pred)
        self.y_preds = np.array(labels_pred, dtype = np.int32)
        
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self) -> np.ndarray:
        return confusion_matrix(self.y_test, self.y_preds)

    @classmethod
    def load_csv(csv_path : str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        dataset = pd.read_csv(csv_path, delimiter = ',', engine='python')
        dataset = dataset.sample(frac=1, random_state = 42)
        x, y = dataset[:, :4],dataset[:, -1]
        return x, y