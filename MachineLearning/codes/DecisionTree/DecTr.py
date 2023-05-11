from typing import Any
import numpy as np
import pandas as pd
from collections import Counter


def pmf_with_elements(partition: np.ndarray) -> tuple[np.ndarray, list[Any]]:
    """
    Get the pmf of a finite partition and a list of elements
    :param partition: The finite set storing the info of a partition
    :return: The pmf and elements
    """
    p = []
    elements = []
    for ele in partition:
        if ele in elements:
            continue
        else:
            elements.append(ele)
            p.append(np.sum(partition == ele) / len(partition))
        if np.sum(p) >= 1:
            break
    return np.array(p), elements


def get_pmf(partition: np.ndarray) -> np.ndarray:
    return pmf_with_elements(partition)[0]


def entropy(partition: np.ndarray):
    p = get_pmf(partition)
    return np.sum(-p * np.log2(p))


def cond_entropy(partition_a: np.ndarray, partition_b: np.ndarray):
    res = 0
    p_b, element_b = pmf_with_elements(partition_b)
    for i in range(len(element_b)):
        ele_b = element_b[i]
        res += p_b[i] * entropy(partition_a[partition_b == ele_b])
    return res


def info_gain(partition_a: np.ndarray, partition_b: np.ndarray):
    return entropy(partition_a) - cond_entropy(partition_a, partition_b)


def info_gain_ratio(partition_a: np.ndarray, partition_b: np.ndarray):
    if entropy(partition_b) == 0:
        return 0
    else:
        return info_gain(partition_a, partition_b) / entropy(partition_b)


def precision(y_test: np.ndarray, y_pred: np.ndarray):
    return np.sum(y_test * y_pred) / np.sum(y_pred)


def recall(y_test: np.ndarray, y_pred: np.ndarray):
    return np.sum(y_test * y_pred) / np.sum(y_test)


def F1score(y_test: np.ndarray, y_pred: np.ndarray):
    return np.sum(y_test * y_pred) * 2 / (np.sum(y_pred) + np.sum(y_test))


class Node:
    def __init__(self, feature_type, feature_val, label=None):
        """
        The node of a tree
        :param feature_type: The feature type that the node stores now
        :param feature_val: The value of feature that the node represent now
        :param label: The label of the leaf node while internal node keeps it as None
        """
        self.children = {}
        self.feature_type = feature_type
        self.feature_val = feature_val
        self.label = label

    def __repr__(self):
        return '{}'.format({'label': self.label, 'value': str(self.feature_type) + ': ' + str(self.feature_val),
                            'tree': self.children})

    def add_node(self, feature_name, feature_val=None, feature_type=None, label=None):
        self.children[feature_name] = Node(feature_val, feature_type, label)

    def delete_node(self, feature_val, feature_type):
        if self.feature_type == feature_type:
            self.children.pop(feature_val)
        else:
            for key in self.children.keys():
                self.children[key].delete_node(feature_val, feature_type)

    def get_node_number(self):
        tmp = 1
        if len(self.children) == 0:
            return tmp
        else:
            for key in self.children.keys():
                tmp += self.children[key].get_node_number()
            return tmp


def is_bottom(node: Node) -> bool:
    """
    Detect whether the children of the node is leaf nodes
    :param node: The node that will be detected
    :return: True for yes and False for no
    """
    for key in node.children.keys():
        if len(node.children[key].children) != 0:
            return False
    return True


class DecisionTree:
    def __init__(self, info_rate_lower_bound=0.01, info_lower_bound=0.01, alpha=1):
        """
        The machine learning model of Decision tree.
        :param info_rate_lower_bound: The minimum info gain that the decision tree tolerates.
        :param alpha: The complexity burden parameter
        """
        self._info_rate_lb = info_rate_lower_bound
        self._info_lb = info_lower_bound
        self._alpha = alpha
        self._tree = None

    def fit(self, X: pd.DataFrame, y):
        """
        Fit the model by feature X and label y.
        :param X: Input feature set with multiple features
        :param y: labels
        """
        node = Node(None, None)
        self._tree = self._train(node, X, y)

    def _train(self, node, X: pd.DataFrame, y: np.ndarray) -> Node:
        counter = Counter(y)
        node.label = counter.most_common(1)[0][0]
        if len(np.unique(y)) == 1 or X.empty:
            return node

        info_ratio = 0
        feature_type = None
        col = X.columns
        for feature in col:
            temp = info_gain_ratio(y, np.array(X[feature]))
            if temp > info_ratio:
                info_ratio = temp
                feature_type = feature

        if info_ratio < self._info_rate_lb:
            return node
        else:
            new_X = X.drop(columns=feature_type)
            temp = Counter(X[feature_type]).most_common(None)

            node.feature_type = feature_type
            node.feature_val = [temp[i][0] for i in range(len(temp))]
            for element in temp:
                feature_val = element[0]
                node.add_node(feature_val)
                node.children[feature_val] = self._train(node.children[feature_val],
                                                         new_X[X[feature_type] == feature_val],
                                                         y[X[feature_type] == feature_val])
            return node

    def pruning(self, X: pd.DataFrame, y: np.ndarray):
        """
        Prune the decision tree
        :param X: Train set X where each column stands for one feature
        :param y: Label set y
        """
        self._cut(X, y, self._tree)

    def _cost(self, X: pd.DataFrame, y: np.ndarray, node=None):
        if node is None:
            node = self._tree
            tmp = self._alpha * node.get_node_number()
            if len(node.children) == 0:
                return tmp + entropy(y) * len(y)
            else:
                for key in node.children.keys():
                    sep = X[node.feature_type] == key
                    tmp += self._cost(node=node.children[key], X=X[sep], y=y[sep])
                return tmp
        else:
            if len(node.children) == 0:
                return entropy(y) * len(y)
            else:
                tmp = 0
                for key in node.children.keys():
                    sep = X[node.feature_type] == key
                    tmp += self._cost(node=node.children[key], X=X[sep], y=y[sep])
                return tmp

    def _cut(self, X: pd.DataFrame, y: np.ndarray, node):
        if len(node.children) == 0:
            return

        if not is_bottom(node):
            for key in node.children.keys():
                self._cut(X, y, node.children[key])

        save = node.children
        cost_before = self._cost(X, y)
        node.children = {}
        cost_after = self._cost(X, y)
        if cost_before <= cost_after:
            node.children = save
        return

    def predict(self, X: pd.DataFrame, node=None):
        """
        Predict the labels by test set X
        :param X: Test set
        :param node: No need to be given as a user
        :return: The prediction sequence of given data X
        """
        if node is None:
            node = self._tree
        if len(node.children) == 0:
            predict_seq = np.array([node.label] * X.shape[0])
        else:
            predict_seq = np.zeros(X.shape[0])
            for key in node.children.keys():
                sep = X[node.feature_type] == key
                predict_seq[sep] = self.predict(X[sep], node.children[key])
        return predict_seq

    def score(self, X_test: pd.DataFrame, y_test, show=False):
        """
        Get the evaluation of the decision tree if it is a binary classification model. And the precision rate, recall
        rate and F1 score will be shown.
        :param X_test: test features
        :param y_test: test labels
        :return: precision rate, recall rate and F1 score.
        :param show: The option of whether print these numbers
        """
        y_pred = self.predict(X_test)
        p = precision(y_test, y_pred)
        r = recall(y_test, y_pred)
        F1 = F1score(y_test, y_pred)
        if show:
            print('P=', p)
            print('R=', r)
            print('F1 score=', F1)
        return p, r, F1

    def get_node_num(self):
        return self._tree.get_node_number()
