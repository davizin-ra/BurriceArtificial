# -*- coding: utf-8 -*-
# train_model.py
# Responsável pelo TF-IDF, treino, teste, métricas

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def treinar_modelo(ds):
    X_train, X_test, Y_train, Y_test = train_test_split(
        ds["limpo"],
        ds["label"],
        test_size=0.2,
        random_state=42
    )

    vectorizer = TfidfVectorizer()
    X_trainVet = vectorizer.fit_transform(X_train)
    X_testVet = vectorizer.transform(X_test)

    model = LogisticRegression()
    model.fit(X_trainVet, Y_train)

    Ypred = model.predict(X_testVet)

    accuracy = accuracy_score(Y_test, Ypred)
    print("Accuracy:", accuracy)
    print(classification_report(Y_test, Ypred))
    
    cm = confusion_matrix(Y_test, Ypred)
    print(cm)

    ConfusionMatrixDisplay.from_estimator(
        model,
        X_testVet,
        Y_test,
        cmap=plt.cm.Reds,
        normalize='true'
    )
    plt.show()

    return model, vectorizer, X_train, X_test, Y_train, Y_test