# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| message: false
#| warning: false

import os
import pathlib
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Diretório raiz do projeto
os.chdir('C:/Users/user/Desktop/EAE1106')
raiz = pathlib.Path('projeto_empirico')

# Estrutura de diretórios
diretorios = [
    raiz / 'dados',
    raiz / "dados" / "original",
    raiz / "dados" / "secundario",
    raiz / "scripts",
    raiz / "resultados"
]

# Criação dos diretórios
for diretorio in diretorios:
    diretorio.mkdir(parents=True, exist_ok=True)

print(f"Estrutura criada em: {raiz.resolve()}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
