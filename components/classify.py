# -*- coding: utf-8 -*-
# classify.py
# Responsável pelas funções de classificação do texto

from train_model import treinar_modelo

# Recebe modelo e vectorizer para classificar texto
def classFunc(text, model, vectorizer):
    vet = vectorizer.transform([text])
    pred = model.predict(vet)
    return pred[0]

def ClassFuncLin(lines, model, vectorizer):
    results = []
    for line in lines:
        label = classFunc(line, model, vectorizer)
        results.append((line, label))
    return results

def Organizado(lines, model, vectorizer):
    results = ClassFuncLin(lines, model, vectorizer)
    agrupado = {}
    for linha, label in results:
        if label not in agrupado:
            agrupado[label] = []
        agrupado[label].append(linha)
    return agrupado