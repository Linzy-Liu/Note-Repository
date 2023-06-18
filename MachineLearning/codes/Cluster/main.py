import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import cluster

seed = random.randint(0, 100000000)


# seed = 30907883

def find_proper_k_kmeans(data: np.ndarray, k_range: tuple = (2, 10), distance_type: str = 'euclidean',
                         distance_param=None):
	"""
	Find a proper k for k-means algorithm according to silhouette score and SSE

	:param data: The data to be clustered
	:param k_range: The range of k
	:param distance_type: The type of distance, can be 'euclidean', 'minkowski', 'correlation', 'cosine' and 'mahalanobis'
	:param distance_param: The parameter of distance, for 'minkowski' it's p, for 'mahalanobis' it's the inverse of covariance matrix
	"""
	score = []
	SSE = []
	for k in range(*k_range):
		model = cluster.KMeans(k=k, distance_type=distance_type, distance_param=distance_param, random_state=seed)
		model.fit(data)
		cls = model.clusters

		# Calculate silhouette score
		labels = np.zeros(data.shape[0])
		for i in range(len(cls)):
			labels[cls[i]] = i
		dis = cluster.get_distance_list(data, distance_type, distance_param)
		score.append(silhouette_score(dis, labels, metric='precomputed'))

		# Calculate SSE
		centroids = model.centroids
		SSE.append(cluster.sum_of_distance_error(data, cls, centroids, distance_type, distance_param))

	plt.rc('text', usetex=True)
	fig = plt.figure()
	axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	axe_r = axe.twinx()
	tmp1 = axe.plot(range(*k_range), score, 'ro-', label='Silhouette Score')
	tmp2 = axe_r.plot(range(*k_range), SSE, 'bo-', label='SSE')
	axe.set_xlabel('$k$')
	axe.set_ylabel('Silhouette Score')
	axe_r.set_ylabel('SSE')

	lns = tmp1 + tmp2
	labs = [l.get_label() for l in lns]
	axe.legend(lns, labs, loc='best')

	plt.savefig('kmeans.png', dpi=300)
	plt.show()


def find_proper_k_HC(data: np.ndarray, k_range: tuple = (2, 10), distance_type: str = 'euclidean', distance_param=None,
                     linkage='single'):
	"""
	Find a proper k for hierarchical clustering algorithm according to silhouette score and SSE

	:param data: The data to be clustered
	:param k_range: The range of k
	:param distance_type: The type of distance, can be 'euclidean', 'minkowski', 'correlation', 'cosine' and 'mahalanobis'
	:param distance_param: The parameter of distance, for 'minkowski' it's p, for 'mahalanobis' it's the inverse of covariance matrix
	:param linkage: The type of linkage, can be 'single', 'complete', 'average', 'centroid'
	"""
	score = []
	SSE = []
	for k in range(*k_range):
		model = cluster.HierarchicalCluster(k=k, distance_type=distance_type, distance_param=distance_param,
		                                    linkage=linkage)
		model.fit(data)
		cls = model.clusters
		center = np.zeros((k, data_std.shape[1]))
		for i in range(k):
			center[i] = np.mean(data_std[cls[i]], axis=0)

		# Calculate scores
		labels = np.zeros(data.shape[0])
		for i in range(len(cls)):
			labels[cls[i]] = i
		dis = cluster.get_distance_list(data, distance_type, distance_param)
		score.append(silhouette_score(dis, labels, metric='precomputed'))
		SSE.append(cluster.sum_of_distance_error(data, cls, center, distance_type, distance_param))

	plt.rc('text', usetex=True)
	fig = plt.figure()
	axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	tmp1 = axe.plot(range(*k_range), score, 'ro-', label='Silhouette Score')
	axe_r = axe.twinx()
	tmp2 = axe_r.plot(range(*k_range), SSE, 'bo-', label='SSE')
	axe.set_xlabel('$k$')
	axe.set_ylabel('Silhouette Score')
	axe_r.set_ylabel('SSE')

	lns = tmp1 + tmp2
	labs = [l.get_label() for l in lns]
	axe.legend(lns, labs, loc='best')

	plt.savefig('HierarchicalCluster.png', dpi=300)
	plt.show()


def get_result_kmeans(data_std: np.ndarray, k: int = 2, distance_type: str = 'euclidean', distance_param=None):
	"""
	Get the result of k-means algorithm. The result will be plotted in 2D space, and the silhouette score and SSE will be printed.

	:param data_std: The data to be clustered
	:param k: The number of clusters
	:param distance_type: The type of distance, can be 'euclidean', 'minkowski', 'correlation', 'cosine' and 'mahalanobis'
	:param distance_param: The parameter of distance, for 'minkowski' it's p, for 'mahalanobis' it's the inverse of covariance matrix
	"""
	model = cluster.KMeans(k=k, distance_type=distance_type, random_state=seed, distance_param=distance_param)
	model.fit(data_std)
	cls = model.clusters
	center = model.centroids
	label = np.zeros(data_std.shape[0])
	for i in range(len(cls)):
		label[cls[i]] = i

	# Calculate scores
	dis = cluster.get_distance_list(data_std, distance_type, distance_param)
	score = silhouette_score(dis, label, metric='precomputed')
	sse = cluster.sum_of_distance_error(data_std, cls, center, distance_type, distance_param)
	print('Silhouette Score: {}'.format(score))
	print('SSE: {}'.format(sse))

	# Plot
	full_data = np.concatenate((data_std, center), axis=0)
	tsne = TSNE(random_state=None)
	tsne.fit_transform(full_data)

	new_data = tsne.embedding_[:data_std.shape[0]]
	new_center = tsne.embedding_[data_std.shape[0]:]
	new_data = np.c_[new_data, label]

	fig = plt.figure()
	axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	axe.set_title('KMeans')
	axe.grid(visible=True, linestyle='-.', linewidth=0.25)
	axe.scatter(new_data[:, 0], new_data[:, 1], c=new_data[:, 2], cmap='rainbow')
	axe.scatter(new_center[:, 0], new_center[:, 1], c='black', marker='x')
	plt.savefig('kmeans_result.png', dpi=300)
	plt.show()


def get_result_HC(data_std: np.ndarray, k: int = 2, distance_type: str = 'euclidean', distance_param=None,
                  linkage='single'):
	model = cluster.HierarchicalCluster(k=k, distance_type=distance_type, distance_param=distance_param,
	                                    linkage=linkage)
	model.fit(data_std)
	cls = model.clusters
	label = np.zeros(data_std.shape[0])
	for i in range(len(cls)):
		label[cls[i]] = i
	center = np.zeros((k, data_std.shape[1]))
	for i in range(k):
		center[i] = np.mean(data_std[cls[i]], axis=0)
	dis = cluster.get_distance_list(data_std, distance_type, distance_param)

	print('SSE: {}'.format(cluster.sum_of_distance_error(data_std, cls, center, distance_type, distance_param)))
	print('Silhouette Score: {}'.format(silhouette_score(dis, label, metric='precomputed')))

	tsne = TSNE(random_state=None)
	tsne.fit_transform(data_std)
	new_data = np.c_[tsne.embedding_, label]

	fig = plt.figure()
	axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	axe.set_title('Hierarchical Cluster')
	axe.grid(visible=True, linestyle='-.', linewidth=0.25)
	axe.scatter(new_data[:, 0], new_data[:, 1], c=new_data[:, 2], cmap='rainbow')
	plt.savefig('HC_result.png', dpi=300)
	plt.show()


if __name__ == '__main__':
	# np.seterr(all='raise')
	source = pd.read_excel('农村居民人均可支配收入来源2016.xlsx', index_col=0)
	data = source.values

	data_std = StandardScaler().fit_transform(data)
	# data_std = MinMaxScaler().fit_transform(data)

	S_inv = np.linalg.inv(np.cov(data_std.T))
	# find_proper_k_kmeans(data_std, k_range=(3, 10), distance_type='mahalanobis', distance_param=S_inv)
	get_result_kmeans(data_std, k=5, distance_type='mahalanobis', distance_param=S_inv)
	# find_proper_k_HC(data_std, k_range=(2, 11), distance_type='euclidean', linkage='single')
	# get_result_HC(data_std, k=4, distance_type='euclidean', linkage='single')
	print('seed: {}'.format(seed))
