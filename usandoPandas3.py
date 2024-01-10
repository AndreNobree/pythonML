import pandas as pd 
import os

def pulaLinha():
    print("\n\n")

dados = pd.read_csv('C:/Users/ae2139/Desktop/dev-and/Python/machineLearnig/Contas a serem pagas.csv')

# vai mudar o titulo apenas visualmente, ele não vai alterar nada no arquivo principal
mudaTitulo = dados.rename(columns={'Tags': 'Situacao'})

print(mudaTitulo.head())

pulaLinha()

# conta quantos dados são iguais e mostra eles
print(dados['Vencimento'].value_counts())

pulaLinha()

# faz uma descrição da coluna 'Valor'
print(dados['Valor'].describe())

pulaLinha()

# para exluir uma coluna usa-se 'drop' e informamos a coluna a ser excluída
excluiColuna = dados.drop('Vencimento', axis=1)
# 'axis=1' informa que vamos excluir uma coluna. 'axis=0' informa a linha que vai ser exluida

print(excluiColuna)