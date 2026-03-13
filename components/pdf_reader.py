# -*- coding: utf-8 -*-
# pdf_reader.py
# Responsável por abrir PDF e extrair texto

from PyPDF2 import PdfReader

def ler_pdf(caminho):
    with open(caminho, "rb") as pdf:
        reader = PdfReader(pdf)
        npaginas = len(reader.pages)
        texto_total = ""
        for i in range(npaginas):
            page = reader.pages[i]
            texto_total += page.extract_text() + "\n"
    return texto_total

# Teste
if __name__ == "__main__":
    texto = ler_pdf("data/curriculo.pdf")
    json_texto = texto.split("\n")
    print(json_texto)