#funções diversas utilizadas ao longo dos códigos

import pandas as pd
import networkx as nx
import numpy as np

def make_array(arquivo,aba,coluna):
    df = pd.read_excel(arquivo,sheet_name=aba)
    valores = df[coluna].to_list()
    return valores

def ler_csv(caminho):
    dataframe = pd.read_csv(caminho,sep=',',index_col=0)
    grafo = nx.from_pandas_adjacency(dataframe)
    return grafo

def grau_medio(grafo):
    graus = [grau for _, grau in grafo.degree()]
    grau_medio = np.mean(graus)
    return grau_medio

def calcular_diametros(grafo):
    componentes = list(nx.connected_components(grafo))
    diametros = []
    
    for componente in componentes:
        subgrafo = grafo.subgraph(componente)
        diametros.append(nx.diameter(subgrafo))
        
    diametros.sort(reverse=True)
    
    return diametros