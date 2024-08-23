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
    graumean = sum(dict(grafo.degree(weight="weight")).values())
    return graumean / grafo.number_of_nodes()

def calcular_diametros(grafo):
    componentes = list(nx.connected_components(grafo))
    diametros = []
    
    for componente in componentes:
        subgrafo = grafo.subgraph(componente)
        diametros.append(nx.diameter(subgrafo,weight="weight"))
        
    diametros.sort(reverse=True)
    
    return diametros

def salvar_resultados(caracteristicas, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"Número de nós: {caracteristicas['nós']}\n")
        arquivo.write(f"Conectividade de Nós: {caracteristicas['conectividade_de_nós']}\n")
        arquivo.write(f"Número de arestas: {caracteristicas['arestas']}\n")
        arquivo.write(f"Conectividade de Arestas: {caracteristicas['conectividade_de_arestas']}\n\n")
        
        arquivo.write(f"Densidade do grafo: {caracteristicas['densidade']:.4f}\n")
        arquivo.write(f"Grau médio do grafo: {caracteristicas['grau_medio']:.4f}\n")
        arquivo.write(f"Coeficiente médio de agrupamento: {caracteristicas['clustering_medio']:.4f}\n\n")
        
        arquivo.write(f"Tamanho do maior componente conexo: {caracteristicas['maior_componente']}\n")
        if len(caracteristicas['diametros']) == 1:
            arquivo.write(f"Diâmetro do grafo: {caracteristicas['diametros'][0]}\n\n")
        else:
            for i, diametro in enumerate(caracteristicas['diametros']):
                arquivo.write(f"Diâmetro do componente conexo {i + 1}: {diametro}\n")
            arquivo.write("\n")
        
        arquivo.write("\nCoeficiente de Agrupamento por Nó:\n")
        for node, clustering in caracteristicas['clustering'].items():
            arquivo.write(f"  Nó {node}: {clustering:.4f}\n")

        arquivo.write(f"Centralidade de Proximidade:\n")
        for node, centralidade in caracteristicas['centralidade_de_proximidade'].items():
            arquivo.write(f"  Nó {node}: {centralidade:.4f}\n")
        
        arquivo.write(f"\nCentralidade de Intermediabilidade:\n")
        for node, centralidade in caracteristicas['centralidade_de_intermedialidade'].items():
            arquivo.write(f"  Nó {node}: {centralidade:.4f}\n")