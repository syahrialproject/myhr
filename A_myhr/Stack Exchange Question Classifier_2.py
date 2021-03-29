import json, pandas as pd, numpy as np

from nltk import NaiveBayesClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

topic,ques,excerpt=[],[],[]
i=0
with open('training.json',encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if i==0:
            n=int(data)
        else:
             topic.append(data['topic'])
             ques.append(data['question'])
             excerpt.append(data['excerpt'])
        i=i+1
df=pd.DataFrame(zip(topic, ques,excerpt),columns=['Topic','Questions','Excerpts'])
y=np.array(topic)
X=np.array(excerpt)
print(X.shape,y.shape)

model = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
model.fit(X,y)

_test=[]
for i in range(int(input())):
    h=json.loads(input())
    _test.append(h['excerpt'])
predicted=model.predict(_test)
for i in predicted:
    print(i)