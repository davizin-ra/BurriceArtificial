# -*- coding: utf-8 -*-
# preprocessing.py
# Responsável por limpar o texto e aplicar no dataset

import re
import pandas as pd

def prep(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-zA-Z0-9\s]", "", texto)
    tokens = texto.split()
    return " ".join(tokens)

def aplicar_limpeza_csv(caminho_csv):
    ds = pd.read_csv(caminho_csv)
    ds["limpo"] = ds["text"].apply(prep)
    return ds

# Teste
if __name__ == "__main__":
    ds = aplicar_limpeza_csv("/data/dataset3.csv")
    print(ds.head())