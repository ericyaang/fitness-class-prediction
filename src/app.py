import streamlit as st
import pandas as pd
import numpy as np

def load_data():
    np.random.seed(42)
    n = 100
    data = {
        'booking_id': np.arange(1, n+1),
        'category': np.random.choice(['Yoga', 'Aqua', 'Strength', 'HIIT', 'Cycling'], n),
        'day_of_week': np.random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], n),
        'time': np.random.choice(['AM', 'PM'], n),
        'attended': np.random.choice([0, 1], n)
    }
    return pd.DataFrame(data)

data = load_data()

# Título e descrição
st.title("Sistema de Lista de Espera Dinâmica - GoalZone")
st.write("Verifique as previsões de comparecimento e gerencie a lista de espera.")

# Seleção de Aula
category = st.selectbox('Selecione a categoria da aula:', ['Yoga', 'Aqua', 'Strength', 'HIIT', 'Cycling'])
day = st.selectbox('Selecione o dia da semana:', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
time = st.selectbox('Selecione o horário:', ['AM', 'PM'])

# Filtrando os dados com base na seleção
filtered_data = data[(data.category == category) & (data.day_of_week == day) & (data.time == time)]

# Visualização de Previsões (aqui estamos simulando a previsão, mas no uso real, o modelo seria chamado)
st.write(f"Total de alunos que reservaram: {len(filtered_data)}")
st.write(f"Previsão de alunos que comparecerão: {filtered_data['attended'].sum()}")

# Gerenciamento da Lista de Espera
st.write("Alunos na lista de espera:")
for booking_id in filtered_data[filtered_data.attended == 0]['booking_id']:
    st.write(booking_id)

# Notificação manual (em um aplicativo real, isso enviaria uma notificação)
if st.button('Notificar aluno selecionado'):
    st.write("Aluno notificado com sucesso!")

# Footer
st.write("Para suporte ou mais informações, entre em contato conosco.")
