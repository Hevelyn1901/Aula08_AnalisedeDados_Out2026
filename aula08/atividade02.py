numeros = []

while True:
    numero = int(input('Informe o numero: '))
    numeros.append(numero)
    
    resposta = input('\nQuer continuar [S/N]? ').upper()
    
    if resposta == 'N':
        break

quantidade = len(numeros)
print(f'Total de elementos: {quantidade}')