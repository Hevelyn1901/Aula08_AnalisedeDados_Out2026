# TUPLAS
# Coleção imutavel
# Permite elementos duplicados
# Permite acesso pelo indice
# Mantem ordem de inserção

frutas = ('uva', 'maça', 'morango', 'laranja', 'pera')
print(frutas[1])
print(frutas)

# frutas[1] = 'melancia' # A tupla não pode ser alterada

numeros = (10, 20, 50, 20, 30, 10, 40)
print(numeros.count(20))
print(frutas.index('laranja'))