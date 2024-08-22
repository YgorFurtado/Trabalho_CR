#Criar lista importavel pelo gephi, onde é criado um verice entre todos os bairros de uma determinada linha

import pandas as pd
import ygorfuncoes as yf
from itertools import combinations

rotas_onibus = yf.make_array("database/linhas.xlsx", "bairros", "Bairros")

bairros = set()

for rota in rotas_onibus:
    bairros.update(rota.split('-'))

bairros = sorted(bairros)

arestas = {}

indice_bairro = {bairro: idx for idx, bairro in enumerate(bairros)}

for rota in rotas_onibus:
    bairros_rota = rota.split('-')
    for u, v in combinations(bairros_rota, 2):
        if (u, v) in arestas:
            arestas[(u, v)] += 1
        elif (v, u) in arestas:
            arestas[(v, u)] += 1
        else:
            arestas[(u, v)] = 1

dados = [(u, v, peso) for (u, v), peso in arestas.items()]

df = pd.DataFrame(dados, columns=["Source", "Target", "Weight"])

df.to_csv('Database/lista_gephi2.csv', index=False)