import os
import pandas as pd

# Lê o arquivo Excel
df = pd.read_excel('NomeCompleto+registroid.xlsx')

# Obtém a lista de nomes na coluna 'NOME COMPLETO'
nomes = df['NOME COMPLETO'].tolist()

# Obtém a lista de arquivos PDF na pasta local
arquivos_pdf = [f for f in os.listdir('.') if f.endswith('.pdf')]

# Cria uma lista para armazenar os nomes que estão na coluna 'NOME COMPLETO' mas não nos arquivos PDF
lista = []

# Verifica cada nome na lista de nomes
for nome in nomes:
    # Converte o nome para string
    nome = str(nome)
    # Se o nome não estiver na lista de arquivos PDF, adiciona à lista
    if nome + '.pdf' not in arquivos_pdf:
        # Obtém os valores correspondentes na coluna 'Registro Id'
        registros = df.loc[df['NOME COMPLETO'] == nome, 'Registro Id'].values
        # Verifica se há algum valor antes de tentar acessá-lo
        if registros.size > 0:
            registro = registros[0]
            # Adiciona o nome e o registro à lista
            lista.append((nome, registro))

# Imprime a lista
for item in lista:
    print(f'Nome: {item[0]}, Registro: {item[1]}')
