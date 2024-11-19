import pandas as pd

def load_data(filepath):
    """
    Carrega o arquivo Excel.
    """
    return pd.read_excel(filepath)
