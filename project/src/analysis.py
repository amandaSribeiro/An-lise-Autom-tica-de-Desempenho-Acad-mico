import matplotlib.pyplot as plt

def plot_student_performance(student_data, student_id):
    """
    Gera o gráfico de pizza com o desempenho do aluno por trilha.
    """
    if not student_data.empty:
        labels = student_data['trail']
        sizes = student_data['correct_answers'] / student_data['total_questions'] * 100

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'Desempenho do Aluno {student_id} nas Trilhas')
        plt.show()
