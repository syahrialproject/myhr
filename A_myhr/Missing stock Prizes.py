# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor

N = int(input())

stock_list = []
missing_list = []
dates = []
for i in range(0,N):
    temp = input().split("\t")
    dates.append(datetime.strptime(temp[0], '%m/%d/%Y %H:%M:%S'))
    try:
        stock_list.append(float(temp[1]))
    except:
        stock_list.append(np.nan)
        missing_list.append(int(i))


df_stock = pd.DataFrame({"date":dates,"price":stock_list})
missing_dates = df_stock[df_stock['price'].isnull()]['date'].values
missing_dates = missing_dates.astype('datetime64[D]').astype(int)
missing_dates = [[x] for x in missing_dates]

df_stock = df_stock.dropna()
X= [[x] for x in df_stock['date'].values]
y=  df_stock['price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, shuffle=False)


mdl = SGDRegressor(shuffle=False, max_iter=5000, learning_rate='optimal', random_state=0, n_iter_no_change=30)

mdl.fit(X_train, y_train)

y_pred = mdl.predict(missing_dates)

for pred in y_pred:
    print(pred)
