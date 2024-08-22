#le uma matriz de adjacencia de um grafo, e retorna informações sobre ele

import networkx as nx
import ygorfuncoes as yf

grafo = yf.ler_csv("gephi_matriz1.csv")

def obter_caracteristicas(grafo):
    caracteristicas = {}
    caracteristicas['densidade'] = nx.density(grafo)
    caracteristicas['nós'] = grafo.number_of_nodes()
    caracteristicas['arestas'] = grafo.number_of_edges()
    caracteristicas['maior_componente'] = len(max(nx.connected_components(grafo), key=len))
    caracteristicas['clustering_medio'] = nx.average_clustering(grafo)
    caracteristicas['grau_medio'] = yf.grau_medio(grafo)
    caracteristicas['diametros'] = yf.calcular_diametros(grafo)
    
    return caracteristicas

def exibir_resultados(caracteristicas):
    print(f"Número de nós: {caracteristicas['nós']}")
    print(f"Número de arestas: {caracteristicas['arestas']}")
    print(f"Densidade do grafo: {caracteristicas['densidade']:.4f}")
    print(f"Grau medio do grafo: {caracteristicas['maior_componente']}")
    print(f"Coeficiente médio de agrupamento: {caracteristicas['clustering_medio']:.4f}")
    print(f"Tamanho do maior componente conexo: {caracteristicas['maior_componente']}")
    
    if len(caracteristicas['diametros']) == 1:
        print(f"Diâmetro do grafo: {caracteristicas['diametros'][0]}")
    else:
        for i, diametro in enumerate(caracteristicas['diametros']):
            print(f"Diâmetro do componente conexo {i + 1}: {diametro}")
    

caracteristicas = obter_caracteristicas(grafo)
exibir_resultados(caracteristicas)