import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, learning_rate: float, x_n: int, w=None, b=None, iteration=1000):
        """
        Initialize perceptron
        :param learning_rate:
        :param x_n: The dimension of feature x
        :param w: The initial value of parameter w
        :param b: The initial value of parameter w
        :param iteration: The max number for iteration
        """
        self._alpha = learning_rate
        if w is None:
            self._w = np.zeros(x_n)
        else:
            self._w = w
        if b is None:
            self._b = 0
        else:
            self._b = b
        self._max_iter = iteration  # The maximum iteration divided by the scale of training set
        self.iter = 0

    def hypothesis(self, x):
        return np.sign(np.sum(self._w * x) + self._b)

    def fit(self, data: pd.DataFrame, feature=None):
        """
        Fit the given data and return the proper parameter w and b
        :param feature: The column needed to be trained
        :param data: The training set
        :return: parameter w and b
        """
        if feature is None:
            feature = list(range(data.shape[1] - 1))
        elif len(feature) != len(self._w):
            print("The length of parameter should be identical to the dimension of feature")
            raise IOError
        data = data.iloc[:, feature + [data.shape[1] - 1]]
        for i in range(self._max_iter):
            mistake = 0
            # Shuffle to make the gradient accent more randomly
            temp = list(range(data.shape[0]))
            random.shuffle(temp)
            for j in temp:
                x = np.array(data.iloc[j, :len(self._w)])
                y = data.iloc[j, len(self._w)]
                # stochastic gradient decent
                if self.hypothesis(x) * y <= 0:
                    mistake += 1
                    self._w += self._alpha * y * x
                    self._b += self._alpha * y
            self.iter += 1
            if mistake == 0:
                break
        return self._w, self._b

    def show(self, axe, data: pd.DataFrame, feature: list, param: list):
        """
        Show the learning result
        :param param: The two dimensions that you want to show. For example, [0,1] stands for x1 and x2.
        :param axe: The axe object given by matplotlib
        :param data: The data for presentation, its last column must be the label.
        :param feature: The feature you want to put. For example, [0,1] stands for the 1st and 2nd.
        """
        tmp = data.columns[-1]
        # separate two types
        label_pos = data[data[tmp] == 1]
        label_neg = data[data[tmp] == -1]
        # get the name of two feature
        first = data.columns[feature[0]]
        second = data.columns[feature[1]]

        plt.rc('font', size=10)
        axe.spines[['right', 'top']].set_color(None)
        axe.set_xlabel(first)
        axe.set_ylabel(second)
        axe.set_title('Perceptron Classifier')

        # draw hyperplane
        x = np.linspace(data[first].min() - abs(data[first].min()) * 0.2,
                        data[first].max() + abs(data[first].max()) * 0.2, 100)
        y = -(self._w[param[0]] * x + self._b) / self._w[param[1]]
        axe.plot(x, y, 'r-', label='Hyperplane')

        # draw samples
        axe.plot(label_pos[first], label_pos[second], 'b*', label='setosa')
        axe.plot(label_neg[first], label_neg[second], 'go', label='verginica')
        plt.legend()

    def fit_show(self, axe, data: pd.DataFrame, feature: list, param: list):
        """
        Combines fit and show. It will show the training process
        :param param: The two dimensions that you want to show. For example, [0,1] stands for x1 and x2.
        :param axe: The axe object given by matplotlib
        :param data: The data for presentation and training
        :param feature: The column needed to be trained
        :return: parameter w and b
        """
        if feature is None:
            feature = list(range(data.shape[1] - 1))
        elif len(feature) != len(self._w):
            print("The length of parameter should be identical to the dimension of feature")
            raise IOError

        tmp = data.columns[-1]
        # separate two types
        label_pos = data[data[tmp] == 1]
        label_neg = data[data[tmp] == -1]
        # get the name of two feature
        first = data.columns[feature[0]]
        second = data.columns[feature[1]]
        x_1 = np.linspace(data[first].min() - abs(data[first].min()) * 0.2,
                          data[first].max() + abs(data[first].max()) * 0.2, 100)
        data = data.iloc[:, feature + [data.shape[1] - 1]]

        plt.rc('font', size=10)
        axe.spines[['right', 'top']].set_color(None)
        axe.set_xlabel(first)
        axe.set_ylabel(second)
        axe.set_title('Perceptron Classifier')
        axe.plot(label_pos[first], label_pos[second], 'b*', label='setosa')
        axe.plot(label_neg[first], label_neg[second], 'go', label='verginica')
        line = axe.plot([], [], 'b-', label='hyperplane')[0]

        for i in range(self._max_iter):
            mistake = 0
            temp = list(range(data.shape[0]))
            random.shuffle(temp)
            for j in temp:
                x = np.array(data.iloc[j, :len(self._w)])
                y = data.iloc[j, len(self._w)]
                if self.hypothesis(x) * y <= 0:
                    mistake += 1
                    self._w += self._alpha * y * x
                    self._b += self._alpha * y
                    # draw dynamic changes
                    y_1 = -(self._w[param[0]] * x_1 + self._b) / self._w[param[1]]
                    line.set_data(x_1, y_1)
                    axe.relim()
                    axe.autoscale_view()
                    plt.legend()
                    plt.show()
                    plt.pause(0.01)
            if mistake == 0:
                break
        return self._w, self._b


def show_data(axe, data: pd.DataFrame, feature, w=None, b=None):
    """
    Show the source data.
    :param axe: The axe object given by matplotlib
    :param data: The data for presentation
    :param feature: The feature you want to put. For example, [0,1] stands for the 1st and 2nd.
    :param w: If it is not None, the hyperplane determined by w and b will be drawn. It should be a 2D vector.
    :param b: If it is not None, the hyperplane determined by w and b will be drawn.
    """
    tmp = data.columns[-1]
    # separate two types
    label_pos = data[data[tmp] == 1]
    label_neg = data[data[tmp] == -1]
    # get the name of two feature
    first = data.columns[feature[0]]
    second = data.columns[feature[1]]

    plt.rc('font', size=10)
    axe.spines[['right', 'top']].set_color(None)
    axe.set_xlabel(first)
    axe.set_ylabel(second)
    axe.set_title('Perceptron Classifier')

    if w is not None and b is not None:
        # draw hyperplane
        x = np.linspace(data[first].min() - abs(data[first].min()) * 0.2,
                        data[first].max() + abs(data[first].max()) * 0.2, 100)
        y = -(w[0] * x + b) / w[1]
        axe.plot(x, y, 'r-', label='Hyperplane')

    # draw samples
    axe.plot(label_pos[first], label_pos[second], 'b*', label='setosa')
    axe.plot(label_neg[first], label_neg[second], 'go', label='verginica')
    plt.legend()
    axe.autoscale_view()
