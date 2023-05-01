import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as datasets
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KMeansOnDigits():
    def __init__(self, n_clusters, random_state) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state
        
    def load_dataset(self) -> None:
        self.digits = datasets.load_digits()
    
    def predict(self) -> None:
        self.clusters = KMeans(n_clusters = self.n_clusters, random_state = self.random_state).fit_predict(self.digits.data)
        
    def get_labels(self) -> None:
        result = np.zeros_like(self.clusters)
        for cluster in range(len(np.unique(self.clusters))):
            mask = (self.clusters == cluster)
            subarray = self.digits.target[mask]
            result[mask] = np.bincount(subarray).argmax()
        self.labels = result
        
    def calc_accuracy(self) -> None:
        self.accuracy = np.round(accuracy_score(self.digits.target, self.labels), 2)
        
    def confusion_matrix(self) -> None:
        self.mat = confusion_matrix(self.digits.target, self.labels)