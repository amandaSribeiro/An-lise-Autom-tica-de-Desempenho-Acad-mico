def preprocess_data(data):
    """
    Realiza o pré-processamento dos dados.
    Exemplo: limpeza, normalização ou transformação dos dados.
    """
    # Exemplo de pré-processamento: renomear colunas para letras minúsculas
    data.columns = data.columns.str.lower()
    return data
