import numpy as np
import pandas as pd
from numpy.linalg import norm


def get_index_of_median(obj) -> int:
    med = np.median(obj)
    return np.abs(obj - med).argmin()


class Node:
    def __init__(self, axis, val: np.ndarray, label):
        self.value = val
        self.label = label
        self.axis = axis
        self.left_child = None
        self.right_child = None


class KNearestNeighbors:
    def __init__(self, k):
        """
        The initializer of KNN
        :param k:
        """
        self._KDTree = None
        self._K = k

    def fit(self, X: pd.DataFrame, y):
        """
        Fit the model(Build the KD Tree)
        :param X: Feature set
        :param y: Labels
        """
        axis = 0
        feature = X.columns[axis]
        ind = get_index_of_median(X[feature])
        self._KDTree = Node(axis, val=X.iloc[ind], label=y[ind])
        self._build_tree(X.drop(X.index[ind], axis=0), y.drop(y.index[ind], axis=0))

    def _build_tree(self, X, y, node=None):
        if node is None:
            node = self._KDTree

        # separate
        axis = node.axis
        feature = X.columns[axis]
        index = X[feature] <= node.value[axis]
        X_left = X[index]
        y_left = y[index]
        X_right = X[~index]
        y_right = y[~index]

        axis = (axis + 1) % len(node.value)
        feature = X.columns[axis]
        # left
        if not X_left.empty:
            ind = get_index_of_median(X_left[feature])
            node.left_child = Node(axis, X_left.values[ind], y_left[ind])
            self._build_tree(X_left.drop(X_left.index[ind], axis=0), y_left.drop(y_left.index[ind], axis=0),
                             node.left_child)
        # right
        if not X_right.empty:
            ind = get_index_of_median(X_right[feature])
            node.right_child = Node(axis, X_right.values[ind], y_right[ind])
            self._build_tree(X_right.drop(X_right.index[ind], axis=0), y_right.drop(y_right.index[ind], axis=0),
                             node.right_child)

    def predict(self, X: pd.DataFrame) -> list:
        """
        Predict the test set X
        :param X: The test set
        :return: The list of prediction
        """
        predict_list = []
        for i in range(X.shape[0]):
            feature = X.values[i]
            knn = []

            def _traverse(node: Node):
                if feature[node.axis] <= node.value[node.axis]:
                    if node.left_child is not None:
                        _traverse(node.left_child)
                    if len(knn) < self._K:
                        knn.append([node.label, node.value, norm(node.value - feature)])
                        knn.sort(key=lambda x: x[2])
                    else:
                        dis = norm(node.value - feature)
                        if dis < knn[-1][2]:
                            knn.append([node.label, node.value, dis])
                            knn.sort(key=lambda x: x[2])
                            knn.pop()
                    if knn[-1][2] > node.value[node.axis] - feature[node.axis] and node.right_child is not None:
                        _traverse(node.right_child)
                    return
                else:
                    if node.right_child is not None:
                        _traverse(node.right_child)
                    if len(knn) < self._K:
                        knn.append([node.label, node.value, norm(node.value - feature)])
                        knn.sort(key=lambda x: x[2])
                    else:
                        dis = norm(node.value - feature)
                        if dis < knn[-1][2]:
                            knn.append([node.label, node.value, dis])
                            knn.sort(key=lambda x: x[2])
                            knn.pop()
                    if knn[-1][2] > node.value[node.axis] - feature[node.axis] and node.left_child is not None:
                        _traverse(node.left_child)
                    return

            _traverse(self._KDTree)
            temp = [label for label, _, _ in knn]
            predict_list.append(max(temp, key=temp.count))
        return predict_list
