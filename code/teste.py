import networkx as nx
import ygorfuncoes as yf
num = input()
grafo = yf.ler_csv(f"gephi_matriz{num}.csv")

betweenness = nx.betweenness_centrality(grafo, normalized=True)

sorted_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)

print("Centralidade de cada nó (do maior para o menor):")
for node, centrality in sorted_betweenness:
    print(f"Nó {node}: {centrality:.4f}")
