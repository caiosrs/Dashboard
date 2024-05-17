import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel
excel_file = r'D:\1Desktop\Documentos\My Web Sites\App py\Dashboard\Ocorrências T.I..xlsx'

# Carregar os dados do arquivo Excel
df = pd.read_excel(excel_file, sheet_name='Caio', nrows=3381)

# Filtrar apenas as linhas onde a coluna 'CANAL' contém as palavras desejadas
#dados_filtrados = df[df['CANAL'].str.contains(r'\b(?:Chamado:|Presencial|E-mail|Whatsapp|Ligação)', na=False)]

total_chamados = df['CANAL'].str.count(r'\bChamado:').sum()
total_presencial = df['CANAL'].str.count('Presencial').sum()
total_email = df['CANAL'].str.count('E-mail').sum()
total_whatsapp = df['CANAL'].str.count(r'\bWhatsapp').sum()
total_whatsappp = df['CANAL'].str.count(r'\bWhatsappp').sum()
total_ligacao = df['CANAL'].str.count('Ligação').sum()

# Armazenar os totais em um dicionário
dados_filtrados = {
    'Chamado': total_chamados,
    'Presencial': total_presencial,
    'E-mail': total_email,
    'Whatsapp': total_whatsapp + total_whatsappp,
    'Ligação': total_ligacao
}

# Contagem dos itens relevantes
#contagem = dados_filtrados['CANAL'].value_counts()

# Gráfico de barras
st.bar_chart(dados_filtrados)

# Exibição da contagem
st.write('Contagem de itens da coluna B onde estão "Chamado:", "Presencial", "E-mail", "Whatsapp" e "Ligação":')
st.write(dados_filtrados)
