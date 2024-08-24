import pandas as pd
import igraph as ig

# Load the adjacency matrix from a CSV file
dataframe = pd.read_csv('gephi_lista1.csv', sep=',', index_col=0)

# Convert the DataFrame to numeric, replacing non-numeric values with 0
dataframe_numeric = dataframe.apply(pd.to_numeric, errors='coerce').fillna(0)

# Convert the DataFrame to a numpy array
adj_array = dataframe_numeric.values

# Create an igraph Graph object from the adjacency matrix
g = ig.Graph.Adjacency((adj_array > 0).tolist(), mode=ig.ADJ_UNDIRECTED)

# If the graph has weighted edges, add the weights
if dataframe_numeric.max().max() > 1:
    g.es['weight'] = adj_array[adj_array.nonzero()]

# Add vertex labels from the DataFrame index
g.vs['name'] = dataframe.index.tolist()

# Now g is your igraph Graph object
