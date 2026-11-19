produtos = []  # lista = plural

for i in range(2):
    produto = input ('Informe o nome do produto: ')
    produtos.append(produto) # adiciona na lista produtos

print(produtos)   

# Acesso ao elemento
n = int(input('Digite o indice  do elemnto a acessar: '))
print(produtos[n])  # print(produtos[n-1]) procura o indice de tras para frente


# Alterando uma lista "nome de um elemento"
produtos[n-1] = input(f'Informe o nome do outro elemento na posição {n}: ') # 2
print(produtos)  

# Remover da lista
produto_a_remover = input('\nDigite o nome do produto a remover: ')

if produto_a_remover in produtos: # verificar se o nome do produto existe na lista
    produtos.remove(produto_a_remover)
print(produtos)  