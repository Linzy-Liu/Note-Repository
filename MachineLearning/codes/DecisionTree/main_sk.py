import pandas as pd
import numpy as np
import pydotplus
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import KFold
from sklearn import metrics
import os

os.environ["Path"] += os.pathsep + 'D:/tools/Graphviz/bin/'

if __name__ == '__main__':
    train = pd.read_excel('银行借贷数据集train.xls', index_col=0)
    test = pd.read_excel('银行借贷数据集test.xls', index_col=0)
    tmp = [0, 10000, 20000, 30000, 40000, 50000]
    train['revenue'] = pd.cut(train['revenue'], tmp, labels=False)
    test['revenue'] = pd.cut(test['revenue'], tmp, labels=False)

    # prepare data
    X = train.iloc[:, :-1]
    y = train.iloc[:, -1]
    X_test = test.iloc[:, :-1]
    y_test = test.iloc[:, -1]

    # K-Fold Verification
    kf = KFold(n_splits=10, shuffle=False)
    param = [[i, j] for i in np.arange(1, 7) for j in np.arange(0, 3, 0.1)]
    best_param = None
    best_F1_mean = 0
    for pairs in param:
        model = DecisionTreeClassifier(max_depth=pairs[0], ccp_alpha=pairs[1])
        F1 = []
        for index_train, index_verify in kf.split(X, y):
            X_train = X.iloc[index_train]
            y_train = y.iloc[index_train]
            X_verify = X.iloc[index_verify]
            y_verify = y.iloc[index_verify]

            model.fit(X_train, y_train)
            y_pred = model.predict(X_verify)
            F1.append(metrics.f1_score(y_verify, y_pred))

        tmp = np.mean(F1)
        if best_F1_mean < tmp:
            best_param = pairs
            best_F1_mean = tmp

    print(best_param)
    clf = DecisionTreeClassifier(max_depth=best_param[0], ccp_alpha=best_param[1])
    clf.fit(X, y)
    y_pred = clf.predict(X_test)

    # Evaluation of the model
    print('P=', metrics.precision_score(y_test, y_pred))
    print('R=', metrics.recall_score(y_test, y_pred))
    print('F1=', metrics.f1_score(y_test, y_pred))

    feature = train.columns[:-1]
    class_name = ["will debt", "won't debt"]
    data_dot = export_graphviz(decision_tree=clf, out_file=None, feature_names=feature, class_names=class_name,
                               rounded=True, filled=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(data_dot)
    graph.write_png("debt_motivation.png")
