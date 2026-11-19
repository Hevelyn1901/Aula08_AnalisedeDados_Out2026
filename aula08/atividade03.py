numeros = []

for i in range(12):
    numero = int(input('Informe o numero: '))
    numeros.append(numero)
    
ordenada = sorted(numeros)

print(f'Lista ordenada: {ordenada}')