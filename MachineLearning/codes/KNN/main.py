import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, classification_report
from KNN import KNearestNeighbors

if __name__ == '__main__':
    source = pd.read_excel('北京市空气质量数据train.xlsx', index_col=0)
    test = pd.read_excel('北京市空气质量数据test.xlsx', index_col=0)

    source[source == 0] = np.nan
    source[source['质量等级'] == '无'] = np.nan
    source.dropna(how='any', inplace=True)

    X = source.iloc[:, :-1]
    # X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    y = source.iloc[:, -1]

    """skf = StratifiedKFold(n_splits=10)
    for k in range(2, 13):
        f1s = []
        model = KNearestNeighbors(k=k)
        for train_index, verify_index in skf.split(X, y):
            X_train = X.iloc[train_index]
            y_train = y.iloc[train_index]
            X_verify = X.iloc[verify_index]
            y_verify = y.iloc[verify_index]
            model.fit(X_train, y_train)
            y_pred = model.predict(X_verify)
            f1s.append(f1_score(y_verify, y_pred, average='weighted'))
        print('k=', k, ' average f1=', np.average(f1s), 'f1=', f1s)"""
    model = KNearestNeighbors(k=8)
    model.fit(X, y)

    temp = test.iloc[:, :-1]
    # X_test = (temp - np.mean(temp, axis=0)) / np.std(temp, axis=0)
    X_test = temp
    y_test = test.iloc[:, -1]
    y_pred = model.predict(X_test)
    print('Classification report:')
    print(classification_report(y_test, y_pred))
    print('f1 score=', f1_score(y_test, y_pred, average='weighted'))
