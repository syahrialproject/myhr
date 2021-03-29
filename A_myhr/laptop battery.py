
# Problem: https://www.hackerrank.com/challenges/battery/problem
# Score: 10

# import pandas as pd
# from sklearn.linear_model import LinearRegression


# timeCharged = float(input())
# data = pd.read_csv('trainingdata.txt', names=['charged', 'lasted'])
# train = data[data['lasted'] < 8]
# model = LinearRegression()
# model.fit(train['charged'].values.reshape(-1, 1), train['lasted'].values.reshape(-1, 1))
# ans = model.predict([[timeCharged]])
# # print(min(ans[0][0], 8))
# myans = min(ans[0][0], 8)
# print(round(myans,2))


import pandas as pd
from sklearn.linear_model import LinearRegression

timeCharged = float(input())
data = pd.read_csv('trainingdata.txt', names=['charged','lasted'])
train = data[data['lasted']<8]
X = train['charged'].values.reshape(-1,1)
Y = train['lasted'].values.reshape(-1,1)

model = LinearRegression()
model.fit(X,Y)
myans = model.predict([[timeCharged]])
ans = myans[0][0]

if ans < 8 :
    print (round(ans,2))
else:
    print(8)

