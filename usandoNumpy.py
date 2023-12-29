# numpy é uma biblioteca focada em operações matematicas
import numpy as np

#array simples
a = np.array([1, 2, 3])


#array simples com mais dados
b = np.array([ (2, 5, 7), (3, 9, 7), (10, 23, 43) ])

#essa função vai puxar o maior elemento da matriz
maior = b.max()
#essa função vai puxar o menor elemento da matriz
menor = b.min()
#essa função vai somar todos os elementos da matriz
soma = b.sum()
#essa função vai fazer a media da matriz
media = b.mean()
# essa função vai mostrar o desvio padrão
desvio = b.std()

print(f"Maior elemento: {maior}\n\nMenor elemento: {menor}\n\nSoma de todos os elementos: {soma}\n\nMedia dos elementos: {media}\n\nDesvio padrão: {desvio} ")

# A função "zeros" do numpy vai criar uma "matriz de zeros" de 4 linhas e 5 colunas
c = np.zeros((4, 5))

# A função "ones" do numpy vai criar uma "matriz de 1" de 5 linhas e 6 colunas
d = np.ones((5, 6))

# A função "eye" do numpy vai criar uma "matriz de 0 e 1", onde o "1" vai fica na diagonal
e = np.eye((8))


print(f"\n\n\nExemplo 1:\n{a}\n\nExemplo 2:\n{b}\n\nExemplos de zeros: \n{c}\n\nExemplo de un's:\n{d}\n\nExemplo de eye:\n{e}")
