# SETS "Conjuntos"
# Coleção mutável
# Não garante ordem
# Não permite indice

# Criar sets vazios
dias = set()
dias.add('segunda')
dias.add('terça')
print(dias)


# Conjuntos inicializados
frutas = {'maça', 'uva', 'pera', 'morango', 'laranja'}
print(frutas)
print(type(frutas))

# remover
# frutas.remove('uva')
frutas.remove('morango')
print(frutas)

print(len(frutas)) # conta a quantidade

# converter lista para sets
# lista = [5, 7, 4, 1, 2, 8, 13, 6]
# conjunto_set = set(lista)
# print(conjunto_set)

numeros =[5, 7, 4, 1, 4, 8, 13, 6, 5, 13, 8, 29] # set não aceita numero repetido
conjunto = set(numeros) # converter lista para conjunto set
numeros = list(conjunto) # converte conjunto set lista
print(len(conjunto))
print(conjunto)