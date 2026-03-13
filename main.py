import sys
sys.path.append("./components")

from pdf_reader import ler_pdf
from preprocessing import aplicar_limpeza_csv
from train_model import treinar_modelo
from classify import Organizado

# Ler PDF
texto = ler_pdf("data/curriculo.pdf")
json_texto = texto.split("\n")

# Limpar CSV
ds = aplicar_limpeza_csv("data/dataset3.csv")

# Treinar modelo
model, vectorizer, X_train, X_test, Y_train, Y_test = treinar_modelo(ds)

# Classificar PDF
agrupado = Organizado(json_texto, model, vectorizer)
print(agrupado)