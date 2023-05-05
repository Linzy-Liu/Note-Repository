import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from perceptron import Perceptron

if __name__ == '__main__':
    source = load_iris()
    temp = pd.DataFrame(data=source.data, columns=source.feature_names)
    temp["label"] = source.target
    data = temp[(temp['label'] == 0) | (temp['label'] == 2)]
    data.loc[data['label'] == 0, 'label'] = 1
    data.loc[data['label'] == 2, 'label'] = -1
    feature = [2, 3]  # The feature I chose to train

    LEARNING_RATE = 0.2
    model = Perceptron(LEARNING_RATE, 4)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # Train the model
    w, b = model.fit(data)
    print('w=', w)
    print('b=', b)
    print('iteration=', model.iter)
    model.show(axe, data, feature, [0, 1])
    plt.show()
    '''plt.ion()
    model.fit_show(axe, data, [0, 1], [0, 1])
    plt.pause(5)
    plt.ioff()'''
