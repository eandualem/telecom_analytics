import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.preprocessing import Normalizer, MinMaxScaler


class DfUtils():

    def __init__(self):
        pass

    def normalizer(self, df, columns):
        norm = Normalizer()
        return pd.DataFrame(norm.fit_transform(df), columns=columns)

    def scaler(self, df, columns):
        minmax_scaler = MinMaxScaler()
        return pd.DataFrame(minmax_scaler.fit_transform(df), columns=columns)

    def scale_and_normalize(self, df, columns):
        return self.normalizer(self.scaler(df, columns), columns)

    def choose_kmeans(self, df: pd.DataFrame, num: int):
        distortions = []
        inertias = []
        K = range(1, num)
        for k in K:
            kmeans = KMeans(n_clusters=k, random_state=0).fit(df)
            distortions.append(sum(
                np.min(cdist(df, kmeans.cluster_centers_, 'euclidean'), axis=1)) / df.shape[0])
            inertias.append(kmeans.inertia_)

        return (distortions, inertias)
