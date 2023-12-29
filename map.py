precos_prod = [3000, 5000, 8000, 2000, 10000]

def aplicar_aumento(preco):
    if preco > 6000:
        return preco * 1.1
    else:
        return preco

# o "list" especifica para o "map" que a variavel precos prod é do tipo list
precos_prod = list(map(aplicar_aumento, precos_prod))
# o "map()" funciona como um "for" so que com funções, nesse caso de cima ele pediu a função que ta fazendo o calculo + a lista 
print(precos_prod)