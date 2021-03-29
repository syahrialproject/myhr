import numpy as np
from sklearn import linear_model

def read_input():
    train, test = list(), list()

    F, N = map(int, input().split(' '))
    [train.append(input().split(' ')) for _ in range(0, N)]
    T = int(input())
    [test.append(input().split(' ')) for _ in range(0, T)]

    # Make list indices integers 
    train = np.array(train, dtype=np.float64)
    test = np.array(test, dtype=np.float64)

    x_train = train[:, 0:F]
    y_train = train[:, -1]
    return x_train, y_train, test

x_train, y_train, x_test = read_input()

model = linear_model.LinearRegression()
model.fit(x_train, y_train)
y_test = model.predict(x_test)

for result in y_test:
    print(result)
