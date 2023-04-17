"""
Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
negativo (considere o valor zero como positivo).
"""
num = float(input('Digite um numero: '))

if num >= 0:
    print(f'O numero {num} é Positivo.')
else:
    print(f'O numero {num} é Negativo.')
