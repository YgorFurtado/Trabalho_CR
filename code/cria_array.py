import pandas as pd

def make_array(arquivo,aba,coluna):
    df = pd.read_excel(arquivo,sheet_name=aba)
    valores = df[coluna].to_list()
    return valores
