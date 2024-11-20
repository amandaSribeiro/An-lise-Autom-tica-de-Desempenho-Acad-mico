import matplotlib.pyplot as plt

def analyze_data(student_data, student_id):
    """
    Gera um gráfico de pizza com o desempenho do aluno por trilha,
    garantindo que cada trilha seja agregada de forma única.
    """
    filtered_data = student_data[student_data['student_id'] == student_id]
    
    if not filtered_data.empty:
        # Agrupa os dados por trilha e calcula a média das respostas corretas e do total de perguntas
        grouped_data = filtered_data.groupby('trail').sum()
        grouped_data['percentage'] = grouped_data['correct_answers'] / grouped_data['total_questions'] * 100
        
        # Cria as etiquetas e os tamanhos para o gráfico de pizza
        labels = grouped_data.index
        sizes = grouped_data['percentage']

        # Gera o gráfico de pizza
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'Desempenho do Aluno {student_id} nas Trilhas')
        plt.show()
