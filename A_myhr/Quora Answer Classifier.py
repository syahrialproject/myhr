# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.svm import SVC




n,m=map(int,input().split())

X,y=[],[]
for z in range(n):
    line = input().split()
    y.append(int(line[1]))
    k=2
    res=[]
    for i in line[k:len(line)]:
        k=i.index(":")
        res.append(float(i[k+1:]))
        k=k+1
    X.append(res)

        
q=int(input())
#X=np.array(X)
#y=np.array(y)
#print(X.shape,y.shape)
model = RandomForestClassifier()#Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf',MultinomialNB ())])
X = preprocessing.scale(X)
model.fit(X,y)

X_test=[]
names=[]
for z in range(q):
    line = input().split()
    names.append(line[0])
    k = 1
    res = []
    for i in line[k:len(line) ]:
        k = i.index(":")
        res.append(float(i[k + 1:]))
        k = k + 1
    X_test.append(res)
X_test = preprocessing.scale(X_test)

pred=model.predict(X_test)
for i in range(len(pred)):
    if pred[i]==1:
        print(names[i],"+1")
    else:
        print(names[i],"-1")

