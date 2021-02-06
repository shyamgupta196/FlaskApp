import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import joblib
from sklearn.model_selection import KFold


if __name__ == '__main__':

    # dta = load_iris()
    # data = pd.DataFrame(dta.data, columns=dta.feature_names)
    # data['class'] = dta.target
    # data['class'] = data['class'].map(
    #     {0: 'setosa', 1: 'versicolor', 2: 'verginica'})

    # # splitting the data
    # train = data.iloc[:-30, :]
    # test = data.iloc[-30:, :]

    # x, y = train.iloc[:, :-1], train.iloc[:, -1]
    # skf = KFold(shuffle=True)
    # x.index = range(0, 120, 1)
    # y.index = range(0, 120, 1)
    # for train_index, test_index in skf.split(x):
    #     print(train_index, test_index)
    #     X_train, X_test = x.iloc[train_index, :], x.iloc[test_index, :]
    #     y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # # model building
    # model = GaussianNB()
    # model.fit(X_train, y_train)

    # # since we know the model has accuracy of 95% we do not use predict method here
    # # lets save the model
    # file = open('iris.pkl', 'wb')
    # joblib.dump(model, file)
    
    file = open('iris.pkl','rb')
    model = joblib.load(file)
    print(model.predict([[4.7,3.2,1.3,0.2]]))
