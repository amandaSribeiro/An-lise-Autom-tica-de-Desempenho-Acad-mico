import sys
import os

# Adiciona o diretório "project" ao caminho do Python para garantir que os módulos sejam encontrados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import load_data
from src.preprocess import preprocess_data
from src.analysis import analyze_data

def main():
    # Caminho do arquivo Excel
    file_path = "project/data/train/student_performance_base_data.xlsx"
    
    # Carregar os dados
    data = load_data(file_path)
    
    # Pré-processar os dados
    preprocessed_data = preprocess_data(data)
    
    # Realizar a análise
    analyze_data(preprocessed_data)

if __name__ == "__main__":
    main()
