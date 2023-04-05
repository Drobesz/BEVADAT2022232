import seaborn as sns
import numpy as np
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    
    def __init__(self,k:int,test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio
    
    @property
    def k_neighbors(self):
        return self.k
    
    def train_test_split(self, features: pd.DataFrame, labels: pd.Series) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        self.x_train, self.y_train = features.iloc[ : train_size, :], labels.iloc[ : train_size]
        self.x_test, self.y_test = features.iloc[train_size : train_size+test_size, :], labels.iloc[train_size : train_size+test_size]
    
    def euclidean(self, element_of_x: pd.DataFrame) -> pd.DataFrame:
        return (self.x_train - element_of_x).pow(2).sum(axis=1).pow(1./2)
    
    def predict(self, x_test: pd.DataFrame) -> None:
        labels_pred = []
        for i, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.DataFrame({'distance': distances, 'label': self.y_train})
            distances = distances.sort_values(by=['distance', 'label'])
            label_pred = mode(distances.iloc[:self.k, 1], axis=0).mode
            labels_pred.append(label_pred[0])
        self.y_preds = pd.Series(labels_pred)
        
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self):
        return confusion_matrix(self.y_test,self.y_preds)
    
    def plot_confusion_matrix(confusion_matrix) -> None:
        sns.heatmap(confusion_matrix, annot = True)
    
    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        df = pd.read_csv(csv_path)
        df = df.sample(frac=1, random_state=42)
        x, y = df.iloc[:,:-1], df.iloc[:, -1]
        return x, y
    
    def best_k(self) -> Tuple[int, float]:
        best_accuracy = 0
        best_k = 1
        for k in range(1, 21):
            self.k = k
            self.predict(self.x_test)
            accuracy = self.accuracy()
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k
        return best_k, round(best_accuracy, 2)