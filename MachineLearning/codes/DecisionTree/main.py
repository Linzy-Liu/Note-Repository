import numpy as np
import pandas as pd
import DecTr
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

if __name__ == '__main__':
    train = pd.read_excel('银行借贷数据集train.xls', index_col=0)
    test = pd.read_excel('银行借贷数据集test.xls', index_col=0)
    tmp = [0, 10000, 20000, 30000, 40000, 50000]
    train['revenue'] = pd.cut(train['revenue'], tmp, labels=False)
    test['revenue'] = pd.cut(test['revenue'], tmp, labels=False)

    X_test = test.iloc[:, :-1]
    y_test = test.iloc[:, -1]
    X_train, X_verify, y_train, y_verify = train_test_split(train.iloc[:, :-1], train.iloc[:, -1], test_size=0.2,
                                                            random_state=0)
    """
    p = []
    r = []
    f1 = []
    alphas = np.arange(1.5, 2.6, 0.1)
    for i in alphas:
        model = DecTr.DecisionTree(alpha=i)
        model.fit(X_train, y_train)
        model.pruning(X_train, y_train)
        tmp_p, tmp_r, tmp_f1 = model.score(X_verify, y_verify)
        p.append(tmp_p)
        r.append(tmp_r)
        f1.append(tmp_f1)
    plt.plot(alphas, p, label="precision")
    plt.plot(alphas, r, label="recall")
    plt.plot(alphas, f1, label="F1 score")
    plt.legend()
    plt.savefig("alpha_select.png")
    """
    model = DecTr.DecisionTree(alpha=2)
    model.fit(X_train, y_train)
    model.pruning(X_train, y_train)
    model.score(X_test, y_test, show=True)
