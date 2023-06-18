import numpy as np
from scipy.optimize import minimize
from typing import List


def sample_covariance(X: np.ndarray) -> np.ndarray:
	"""
	Compute the sample covariance matrix of X.

	:param X: A numpy array of shape (n, p) where each row represents a sample
	:return: A numpy array of shape (p, p) representing the sample covariance matrix of X
	"""
	temp = np.cov(X, rowvar=False)
	if np.linalg.matrix_rank(temp) < temp.shape[0]:
		raise ValueError("Warning: The covariance matrix is not full rank. Try to use PCA before clustering.")
	return temp


def minkowski_distance(x: np.ndarray, y: np.ndarray, p: int = 2) -> float:
	"""
	Compute the Minkowski distance between two vectors.

	:param x: A numpy array of shape (n,)
	:param y: A numpy array of shape (n,)
	:param p: The parameter p in Minkowski distance
	:return: The Minkowski distance between x and y
	"""
	return np.linalg.norm(x - y, ord=p)


def mahalanobis_distance(x: np.ndarray, y: np.ndarray, S_inv: np.ndarray) -> float:
	"""
	Compute the Mahalanobis distance between two vectors.

	:param x: A numpy array of shape (n,)
	:param y: A numpy array of shape (n,)
	:param S_inv: The inverse of covariance matrix
	:return: The Mahalanobis distance between x and y
	"""
	return np.sqrt((x - y) @ S_inv @ (x - y).T)


def correlation_distance(x: np.ndarray, y: np.ndarray) -> float:
	"""
	Compute the correlation distance between two vectors.

	:param x: A numpy array of shape (n,)
	:param y: A numpy array of shape (n,)
	:return: The correlation distance between x and y
	"""
	return 1 - np.corrcoef(x, y)[0, 1]


def cosine_distance(x: np.ndarray, y: np.ndarray) -> float:
	"""
	Compute the cosine distance between two vectors.

	:param x: A numpy array of shape (n,)
	:param y: A numpy array of shape (n,)
	:return: The cosine distance between x and y
	"""
	return 1 - x @ y / (np.linalg.norm(x) * np.linalg.norm(y))


def translate_distance(distance_type: str, distance_param=None) -> callable:
	"""
	Translate the distance type to distance function.
	:param distance_type: The type of distance function. It can be 'euclidean', 'minkowski', 'mahalanobis', 'correlation', 'cosine'
	:param distance_param: The parameter of distance function. For 'minkowski', it is p; for 'mahalanobis', it is the inverse of covariance matrix; it is none for other distance functions
	:return: A function that computes the distance between two vectors
	"""
	if distance_type == 'euclidean':
		distance = lambda x, y: minkowski_distance(x, y, 2)
	elif distance_type == 'minkowski':
		if distance_param is None:
			raise ValueError('Invalid distance parameter')
		distance = lambda x, y: minkowski_distance(x, y, distance_param)
	elif distance_type == 'mahalanobis':
		if distance_param is None:
			raise ValueError('Invalid distance parameter')
		distance = lambda x, y: mahalanobis_distance(x, y, distance_param)
	elif distance_type == 'correlation':
		distance = correlation_distance
	elif distance_type == 'cosine':
		distance = cosine_distance
	else:
		raise ValueError('Invalid distance type')
	return distance


def cluster_distance(cluster1: np.ndarray, cluster2: np.ndarray, distance_func: callable, method='min') -> float:
	"""
	Compute the distance between two clusters and compute the distance between one point and a cluster.

	:param cluster1: A numpy array of shape (n1, p) or (n1, )
	:param cluster2: A numpy array of shape (n2, p)
	:param distance_func: A function that computes the distance between two vectors
	:param method: The method to calculate the distance between two clusters. It can be 'min', 'max', 'average', 'centroid'
	:return: The distance between cluster1 and cluster2
	"""
	if method == 'min':
		distance = [distance_func(x, y) for x in cluster1 for y in cluster2]
		return np.min(distance)
	elif method == 'max':
		distance = [distance_func(x, y) for x in cluster1 for y in cluster2]
		return np.max(distance)
	elif method == 'average':
		distance = [distance_func(x, y) for x in cluster1 for y in cluster2]
		return np.mean(distance)
	elif method == 'centroid':
		centroid1 = np.mean(cluster1, axis=0)
		centroid2 = np.mean(cluster2, axis=0)
		return distance_func(centroid1, centroid2)
	else:
		raise ValueError('Invalid method')


class KMeans:
	def __init__(self, k, distance_type='euclidean', distance_param=None, max_iter=1000, tol=1e-4, random_state=None):
		"""
		:param k: The number of clusters
		:param distance_type: The type of distance function. It can be 'euclidean', 'minkowski', 'mahalanobis', 'correlation', 'cosine'
		:param distance_param: The parameter of distance function. For 'minkowski', it is p; for 'mahalanobis', it is the inverse of covariance matrix; it is none for other distance functions
		:param max_iter: The maximum number of iterations
		:param tol: The tolerance of convergence
		:param random_state: The random seed, None for auto random seed. And the given random seed will be used for all random operations.
		"""
		self.centroids = None
		self.clusters = None
		self._k = k
		if distance_type == 'euclidean':
			self._distance_type = 'minkowski'
			self._distance_param = 2
		else:
			self._distance_type = distance_type
			self._distance_param = distance_param
		self._max_iter = max_iter
		self._tol = tol
		self._random_state = random_state

	def fit(self, X: np.ndarray) -> None:
		"""
		Compute k-means clustering.

		:param X: A numpy array of shape (n, p) where each row represents a sample
		:return: None
		"""
		# Initialize distance function
		if self._distance_type == 'mahalanobis':
			self._distance_param = np.linalg.inv(np.cov(X.T))
		distance = translate_distance(self._distance_type, self._distance_param)

		# Initialize centroids with k-means++
		if self._random_state is not None:
			np.random.seed(self._random_state)
		indices = [np.random.randint(0, X.shape[0])]
		for _ in range(1, self._k):
			temp_dis = np.array([cluster_distance(x.reshape(1, -1), X[indices], distance) for x in X])
			p = temp_dis / np.sum(temp_dis)
			p = (p + 1e-10) / np.sum(p + 1e-10)  # Avoid zero probability
			num = np.random.choice(X.shape[0], p=p)
			while num in indices:
				num = np.random.choice(X.shape[0], p=p)
			indices.append(num)
		self.centroids = X[indices]

		# Initialize clusters
		self.clusters = [[] for _ in range(self._k)]
		for i in range(X.shape[0]):
			temp_dis = [distance(self.centroids[j], X[i]) for j in range(self._k)]
			self.clusters[np.argmin(temp_dis)].append(i)

		for _ in range(self._max_iter):
			# Update centroids
			for i in range(self._k):
				if self._distance_type == 'minkowski' and self._distance_param == 2:
					self.centroids[i] = np.mean(X[self.clusters[i]], axis=0)
				else:
					def func(x):
						temp = [distance(X[j], x) for j in self.clusters[i]]
						return np.sum(temp)

					res = minimize(func, self.centroids[i], tol=self._tol)
					self.centroids[i] = res.x

			# Update clusters
			new_clusters = [[] for _ in range(self._k)]
			for i in range(X.shape[0]):
				temp_dis = [distance(self.centroids[j], X[i]) for j in range(self._k)]
				new_clusters[np.argmin(temp_dis)].append(i)
			if np.all([np.all(np.sort(self.clusters[i]) == np.sort(new_clusters[i])) for i in range(self._k)]):
				break
			self.clusters = new_clusters

	def predict(self, X: np.ndarray) -> np.ndarray:
		"""
		Predict the closest cluster each sample in X belongs to.

		:param X: A numpy array of shape (n, p) where each row represents a sample
		:return: A numpy array of shape (n, ) where each element represents the closest cluster index
		"""
		if self.centroids is None:
			raise ValueError('You should fit the model first')
		distance = translate_distance(self._distance_type, self._distance_param)

		return np.array([np.argmin([distance(x, y) for y in self.centroids]) for x in X])


class HierarchicalCluster:
	def __init__(self, k, distance_type='euclidean', distance_param=None, linkage='single'):
		"""
		:param k: The number of clusters
		:param distance_type: The type of distance function. It can be 'euclidean', 'minkowski', 'mahalanobis', 'correlation', 'cosine'
		:param distance_param: The parameter of distance function. For 'minkowski', it is p; for 'mahalanobis', it is the inverse of covariance matrix; it is None for other distance functions
		:param linkage: The type of linkage. It can be 'single', 'complete', 'average', 'centroid'
		"""
		self._k = k
		if distance_type == 'euclidean':
			self._distance_type = 'minkowski'
			self._distance_param = 2
		else:
			self._distance_type = distance_type
			self._distance_param = distance_param
		self._linkage = linkage
		self.clusters = None

	def fit(self, X: np.ndarray) -> None:
		# Initialize distance function
		distance = translate_distance(self._distance_type, self._distance_param)

		# Initialize clusters
		self.clusters = [[i] for i in range(X.shape[0])]
		if self._linkage == 'single':
			method = 'min'
		elif self._linkage == 'complete':
			method = 'max'
		else:
			method = self._linkage
		while len(self.clusters) > self._k:
			temp_dis = np.zeros([len(self.clusters)] * 2)
			for i in range(len(self.clusters)):
				for j in range(i + 1, len(self.clusters)):
					temp_dis[i, j] = cluster_distance(X[self.clusters[i]], X[self.clusters[j]], distance, method)
			temp_dis = np.abs(temp_dis + temp_dis.T) + np.diag([np.inf] * len(self.clusters))
			i, j = np.unravel_index(np.argmin(temp_dis), temp_dis.shape)
			self.clusters[i] += self.clusters[j]
			self.clusters.pop(j)


def sum_of_distance_error(X: np.ndarray, clusters: List[List[int]], centroids: np.ndarray,
                          distance_type: str = 'euclidean', distance_param=None) -> float:
	"""
	Calculate the sum of distance error.

	:param distance_type: The type of distance function. It can be 'euclidean', 'minkowski', 'mahalanobis', 'correlation', 'cosine'
	:param distance_param: The parameter of distance function. For 'minkowski', it is p; for 'mahalanobis', it is the inverse of covariance matrix; it is None for other distance functions
	:param X: A numpy array of shape (n, p) where each row represents a sample
	:param clusters: A list of clusters, each cluster is a list of indices
	:param centroids: A numpy array of shape (k, p) where each row represents a centroid
	"""
	res = 0
	distance = translate_distance(distance_type, distance_param)
	for i in range(len(clusters)):
		res += sum([distance(X[j], centroids[i]) for j in clusters[i]])
	return res


def get_distance_list(X: np.ndarray, distance_type: str = 'euclidean', distance_param=None) -> np.ndarray:
	"""
	Calculate the distance list.

	:param X: A numpy array of shape (n, p) where each row represents a sample
	:param distance_type: The type of distance function. It can be 'euclidean', 'minkowski', 'mahalanobis', 'correlation', 'cosine'
	:param distance_param: The parameter of distance function. For 'minkowski', it is p; for 'mahalanobis', it is the inverse of covariance matrix; it is None for other distance functions
	:return: A numpy array of shape (n, n) where each element represents the distance between two samples
	"""
	distance = translate_distance(distance_type, distance_param)
	res = np.zeros([X.shape[0]] * 2)
	for i in range(X.shape[0]):
		for j in range(i + 1, X.shape[0]):
			res[i, j] = distance(X[i], X[j])
	return res + res.T
