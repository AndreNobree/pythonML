import pandas as pd

alunos = {'Nome': ['Andre', 'Felipe', 'Carla', 'Joyce', 'Francisco'], 'Idade':[23, 23, 25, 25, 62], 'Nota':[6.5, 7.5, 9.6, 10.0, 9.0], 'Aprovado':['não', 'sim', 'sim', 'sim', 'sim']}

# "DataFrame" vai criar uma especie de tabela com as informações que são disponibilizadas
dataf = pd.DataFrame(alunos)

print(f"{dataf}\n\n")

# "Series" cria uma especie de vetor com índicis e sempre é unidimensional
serie = pd.Series([1, 2, 3, 4])

print(serie)