#le uma matriz de adjacencia de um grafo, e retorna informações sobre ele

import networkx as nx
import ygorfuncoes as yf
import matplotlib.pyplot as plt

grafo = yf.ler_csv("gephi_matriz2.csv")

def obter_caracteristicas(grafo):
    caracteristicas = {}
    caracteristicas['nós'] = grafo.number_of_nodes()
    caracteristicas['arestas'] = grafo.number_of_edges()
    caracteristicas['conectividade_de_nós'] = nx.node_connectivity(grafo)    
    caracteristicas['conectividade_de_arestas'] = nx.edge_connectivity(grafo)
    
    caracteristicas['densidade'] = nx.density(grafo)
    caracteristicas['grau_medio'] = yf.grau_medio(grafo)
    caracteristicas['clustering_medio'] = nx.average_clustering(grafo, weight='weight')
    
    caracteristicas['maior_componente'] = len(max(nx.connected_components(grafo), key=len))
    caracteristicas['diametros'] = yf.calcular_diametros(grafo)
    
    caracteristicas['centralidade_de_proximidade']= nx.closeness_centrality(grafo, distance='weight')
    caracteristicas['centralidade_de_intermedialidade'] = nx.betweenness_centrality(grafo, weight='weight')
    caracteristicas['clustering'] = nx.clustering(grafo,weight='weight')
    
    
    return caracteristicas


def exibir_resultados(caracteristicas):
    print(f"Número de nós: {caracteristicas['nós']}")
    print(f"Conectividade de Nós: {caracteristicas['conectividade_de_nós']}")
    print(f"Número de arestas: {caracteristicas['arestas']}")
    print(f"Conectividade de Arestas: {caracteristicas['conectividade_de_arestas']}\n")
    
    print(f"Densidade do grafo: {caracteristicas['densidade']:.4f}")
    print(f"Grau medio do grafo: {caracteristicas['grau_medio']:.4f}")
    print(f"Coeficiente médio de agrupamento: {caracteristicas['clustering_medio']:.4f}\n")
    
    
    print(f"Tamanho do maior componente conexo: {caracteristicas['maior_componente']}")
    if len(caracteristicas['diametros']) == 1:
        print(f"Diâmetro do grafo: {caracteristicas['diametros'][0]}\n")
    else:
        for i, diametro in enumerate(caracteristicas['diametros']):
            print(f"Diâmetro do componente conexo {i + 1}: {diametro}")
        print("\n")
    
    print(f"Clustering: {caracteristicas['clustering']}\n")
    print(f"centralidade_de_proximidade: {caracteristicas['centralidade_de_proximidade']}\n")
    print(f"centralidade_de_intermedialidade: {caracteristicas['centralidade_de_intermedialidade']}\n")

caracteristicas = obter_caracteristicas(grafo)
exibir_resultados(caracteristicas)
yf.salvar_resultados(caracteristicas,nome_arquivo="Resultados2.txt")