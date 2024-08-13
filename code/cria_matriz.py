import pandas as pd
import numpy as np
from cria_array import make_array

rotas_onibus = make_array("database/linhas.xlsx","bairros","Bairros")

bairros = set()
for rota in rotas_onibus:
    bairros.update(rota.split('-'))

bairros = sorted(bairros)

matriz_adj = np.zeros((len(bairros), len(bairros)), dtype=int)

indice_ponto = {ponto: idx for idx, ponto in enumerate(bairros)}

for rota in rotas_onibus:
    bairros_rota = rota.split('-')
    for i in range(len(bairros_rota) - 1):
        u = indice_ponto[bairros_rota[i]]
        v = indice_ponto[bairros_rota[i + 1]]
        matriz_adj[u][v] += 1
        matriz_adj[v][u] += 1

df = pd.DataFrame(matriz_adj, index=bairros, columns=bairros)

df.to_csv('database/matriz.csv')
