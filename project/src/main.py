import sys
import os

# Adiciona o diretório "project" ao caminho do Python para garantir que os módulos sejam encontrados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import load_data
from src.preprocess import preprocess_data
from src.analysis import analyze_data

def main():

    file_path = "../project/data/train/student_performance_base_data.xlsx"
    
    # Verifica se o ficheiro existe
    if os.path.isfile(file_path):
        print("Ficheiro encontrado!")
    else:
        print("Ficheiro não encontrado!")
        return  # Termina a execução se o ficheiro não for encontrado

    # Carregar os dados
    data = load_data(file_path)
    
    # Pré-processar os dados
    preprocessed_data = preprocess_data(data)
    # Realizar a análise
    analyze_data(preprocessed_data, 1)

if __name__ == "__main__":
    main()
