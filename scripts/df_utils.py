import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.preprocessing import StandardScaler, normalize


class DfUtils():

    def __init__(self):
        pass

    def normalizer(self, df):
        data_normalized = normalize(df)
        return data_normalized

    def scaler(self, df):
        scaler = StandardScaler()
        scaled_array = scaler.fit_transform(df)
        return scaled_array

    def scale_and_normalize(self, df):
        return self.normalizer(self.scaler(df))

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
