import pandas as pd
import pickle

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report

Psy = pd.read_csv('Youtube01-Psy.csv')
Katy = pd.read_csv('Youtube02-KatyPerry.csv')
LMFAO = pd.read_csv('Youtube03-LMFAO.csv')
Eminem = pd.read_csv('Youtube04-Eminem.csv')
Shakira = pd.read_csv('Youtube05-Shakira.csv')

data = pd.concat([Psy, Katy, LMFAO, Eminem, Shakira])
data.drop(["COMMENT_ID", "DATE", "AUTHOR"], axis = 1, inplace = True)

x_train, x_test, y_train, y_test = train_test_split(data["CONTENT"], data["CLASS"])

tfidf_vectorizer = TfidfVectorizer(use_idf=True, lowercase=True)
x_train_tfidf = tfidf_vectorizer.fit_transform(x_train)
x_train_tfidf.shape

Model = MultinomialNB()
Model.fit(x_train_tfidf, y_train)

x_test_tfidf = tfidf_vectorizer.transform(x_test)
predictions = Model.predict(x_test_tfidf)

confusion_matrix(y_test, predictions)
print(classification_report(y_test, predictions))

with open("model.pkl", "wb") as model_file:
    pickle.dump(Model, model_file)
with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(tfidf_vectorizer, vectorizer_file)

def model():
    return Model

def vectorizer():
    return tfidf_vectorizer
