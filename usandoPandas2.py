import pandas as pd

def pulaLinha():
    print("\n\n")

alunos = {'Nome': ['Andre', 'Felipe', 'Carla', 'Joyce', 'Francisco'], 'Idade':[23, 23, 25, 25, 62], 'Nota':[6.5, 7.5, 9.6, 10.0, 9.0], 'Aprovado':['não', 'sim', 'sim', 'sim', 'sim']}

# "DataFrame" vai criar uma especie de tabela com as informações que são disponibilizadas
dataf = pd.DataFrame(alunos)
print(dataf)

pulaLinha()

# mostrando a coluna especificada
print(dataf['Aprovado'])

pulaLinha()

# 'loc' vai localizar algo, nesse caso informamos a linha que vai ser printada
print(dataf.loc[[0]])

# localiza as linhas 0, 2 e 4 e printa logo em seguida
print(dataf.loc[[0,2,4]])

# localiza de e até as linhas vão ser printado
print(dataf.loc[0:2])

# localiza uma coluna chamada nome e printa da linha 0 a linha 3 dessa coluna
print(dataf['Nome'].loc[0:3])

# procura na tabela a coluna nome e o dado 'André' vinculada a ela e printa logo em seguida
print(dataf.loc[ dataf['Nome'] == 'Andre' ])

pulaLinha()

# "Series" cria uma especie de vetor com índicis e sempre é unidimensional
serie = pd.Series([1, 2, 3, 4])
print(serie)
pulaLinha()


