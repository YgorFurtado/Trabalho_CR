#Converte uma lista no formato do gephi para uma matriz de adjacencia

import pandas as pd

def csv_to_adjacency_matrix(csv_file, output_file):
    df = pd.read_csv(csv_file)
    
    nodes = sorted(set(df['Source']).union(set(df['Target'])))
    
    adjacency_matrix = pd.DataFrame(0, index=nodes, columns=nodes)
    
    for _, row in df.iterrows():
        source = row['Source']
        target = row['Target']
        weight = row['Weight']
        adjacency_matrix.at[source, target] = weight
        adjacency_matrix.at[target, source] = weight
    
    adjacency_matrix.to_csv(output_file, index=True)
    print(f"salvo em {output_file}")

csv_file = 'gephi_lista2.csv'
output_file = 'gephi_matriz2.csv'
csv_to_adjacency_matrix(csv_file, output_file)