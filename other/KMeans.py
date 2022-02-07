"""
Given a list X of n data points {x1, x2, ..., xn} with dimension d,
divide them into k clusters using k-means clustering algorithm.

Please answer with
1. Pseudo code for the algorithm
2. Implement the algorithm in a function kmeans(X,d,k) in a programming language.
   Return the cluster index of each point. Example input: X = [[1,2], [50, 60], [70, 80], [90, 100]], d = 2, k=2
   Expected output: [0, 1, 1, 1]
3. Time complexity of the algorithm
"""

"""1. Pseudo code
1. initialize k centroids
2. Iteration
2.1 find clusters corresponding to the k centroids
2.2 update centroids based on the cluster mean
3. Stop
3.1 reach max_iterations
3.2 centroids/points do not change within tolerance.
"""

import numpy as np


class KMeans:
    def __init__(self, k, d, max_iters, tolerance):
        self.clusters = [[] for _ in range(k)]
        self.k = k
        self.d = d
        self.max_iters = max_iters
        self._tolerance = tolerance
        self.centroids = []

    def _initialize_centroids(self, k):   # O(n_sample)
        # Randomly choose k points
        random_idxs = np.random.choice(self.n_samples, self.k, replace=False)
        self.centroids = [self.X[i] for i in random_idxs]
        return self.centroids

    def fit(self, X):  # O(max_iters * n_samples * d * k)
        self.X = np.array(X)
        self.n_samples = self.X.shape[0]
        self.centroids = self._initialize_centroids(self.k)
        for i in range(self.max_iters):
            self.clusters = self.create_clusters(self.centroids)
            old_centroids = self.centroids
            self.centroids = self._update_centroids(self.clusters)
            if self._is_converged(old_centroids, self.centroids):
                break
        return self.get_cluster_label(self.clusters)

    def _is_converged(self, old, new):  # O(d * k)
        total_distance = 0
        for i in range(len(old)):
            total_distance += self._distance(old[i], new[i])
        if total_distance < self._tolerance:
            return True
        return False

    @staticmethod
    def _distance(x1, x2):  # O(d)
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def _update_centroids(self, clusters):  # O(d * k)
        centroids = np.zeros((self.k, self.d))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroids[cluster_idx] = cluster_mean
        return centroids

    def create_clusters(self, centroids):
        clusters = [[] for _ in range(self.k)]  # O(k)
        for idx, sample in enumerate(self.X):  # O(n_samples * d * k)
            distances = [self._distance(sample, centroid) for centroid in centroids]
            min_distance_idx = np.argmin(distances)
            clusters[min_distance_idx].append(idx)
        return clusters

    def get_cluster_label(self, clusters):  # O(n_samples * k)
        labels = np.empty(self.n_samples)
        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                labels[sample_idx] = cluster_idx
        return labels

X = [[1,2], [50,60], [70,80], [90,100]]
km = KMeans(2,2,10, .001)
y_pred = km.fit(X)